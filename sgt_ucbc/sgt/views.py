import os

import torch
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from django.core.files.storage import default_storage
import win32com.client as win32
import pythoncom
import pickle
from .forms import MemoireForm, RechercheMemoireForm, SujetDeposerForm
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from django.contrib.auth.decorators import login_required
from .models import Memoire, SujetDeposer, Interaction
from django.db.models import Q
import tensorflow_hub as hub
import pandas as pd
#import tensorflow as tf
from sentence_transformers import SentenceTransformer, util
import nltk
from nltk.translate.bleu_score import sentence_bleu
from rouge_score import rouge_scorer

nltk.download('punkt')
model = SentenceTransformer('all-MiniLM-L6-v2')


def home(request):
    memoires = Memoire.objects.all()
    #memoires = (Memoire.objects.filter(is_published=True) .order_by('-pub_date')[:10])
    data={
        'memoires':memoires
    }
    return render(request, 'sgt/home.html', data)

def about(request):
    return render(request, 'sgt/about_sgt.html')


def memoire_detail(request, memoire_id):
    memoire = get_object_or_404(Memoire, id=memoire_id)
    data = {
        'memoire': memoire
    }
    return render(request, 'sgt/memoire_detail.html', data)

def convert_word_to_pdf(word_file_path):
    """Convertir un fichier Word en PDF."""
    # Initialiser le COM pour Word
    pythoncom.CoInitialize()
    # Chemin pour le fichier PDF converti
    pdf_file_path = word_file_path.replace('.docx', '.pdf')
    # Ouvrir Word
    word = win32.Dispatch('Word.Application')
    word.Visible = False
    # Ouvrir le document
    doc = word.Documents.Open(word_file_path)
    # Convertir en PDF
    doc.SaveAs(pdf_file_path, FileFormat=17)  # 17 est l'ID pour le format PDF
    # Fermer le document et l'application Word
    doc.Close()
    word.Quit()
    return pdf_file_path

@login_required
def ajouter_memoire(request):
    if request.method == "POST":
        form = MemoireForm(request.POST, request.GET)
        if form.is_valid():
            memoire = form.save(commit=False)
            uploaded_file = request.FILES['url_fichier']

            # Sauvegarder temporairement le fichier Word uploadé
            temp_file_path = default_storage.save('temp/' + uploaded_file.name, uploaded_file)

            # Convertir le fichier Word en PDF
            if temp_file_path.endswith('.docx'):
                pdf_file_path = convert_word_to_pdf(temp_file_path)

                # Ouvrir le fichier PDF pour le stocker dans Django
                with open(pdf_file_path, 'rb') as pdf_file:
                    memoire.url_fichier.save(os.path.basename(pdf_file_path), pdf_file)

                # Supprimer les fichiers temporaires après l'upload
                os.remove(temp_file_path)
                os.remove(pdf_file_path)
            Memoire = form.save()
            return redirect(Memoire)
        else:
            #Ajoute ceci pour voir les erreurs de validation dans la console
            print(form.errors)
    else:
        form = MemoireForm
    return render(request, 'sgt/ajouter_memoire.html', {'form': form})



# Je charge le modèle USE (Universal Sentence Encoder)
#embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder-multilingual/3")

#la page de recherche du sujet de mémoire 
@login_required
def compare(request):
    if request.method == 'POST':
        form = RechercheMemoireForm(request.POST)
        if form.is_valid():
            resume = form.cleaned_data['resume']

            # Chargement du modèle sentence-transformers
            model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

            # Récupérer les données de la base de données
            memoires = Memoire.objects.all()
            data = []
            for memoire in memoires:
                data.append({
                    'id': memoire.id,
                    'titre': memoire.titre,
                    'auteur': memoire.auteur,
                    'annee_ac': memoire.annee_ac,
                    'resume': memoire.resume,
                    'cosinus': memoire.cosinus
                })

            df = pd.DataFrame(data)
            df['vecteur'] = df['resume'].apply(lambda x: model.encode(x))  # Générer les embeddings

            # Calcul de similarités
            vecteurs = np.array(df['vecteur'].tolist())
            sim_cos = cosine_similarity(vecteurs)
            indices_cos = np.argsort(-sim_cos, axis=1)

            df['cosinus'] = [list(indices_cos[i, 1:21]) for i in range(len(indices_cos))]

            # Trouver les mémoires similaires
            resume_vecteur = model.encode(resume)  # Générer les embeddings pour le résumé soumis
            sim_resumes = cosine_similarity([resume_vecteur], vecteurs)[0]
            indices_sim_resumes = np.argsort(-sim_resumes)

            memoires_similaires = df.iloc[indices_sim_resumes[1:6]]  # Top 5

            # Calcul des scores BLEU et ROUGE
            bleu_scores = []
            rouge_scores = []
            rouge_scorer_instance = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)

            for i, memoire_similaire in memoires_similaires.iterrows():
                ref_resume = memoire_similaire['resume']

                # Calcul du score BLEU
                bleu_score = sentence_bleu([ref_resume.split()], resume.split())
                bleu_scores.append(bleu_score)

                # Calcul du score ROUGE
                rouge_score = rouge_scorer_instance.score(resume, ref_resume)
                rouge_scores.append(rouge_score)

            # Vérification si le résumé soumis existe dans le DataFrame
            resume_match = df.loc[df['resume'] == resume, 'titre']
            if not resume_match.empty:
                titre = resume_match.values[0]
            else:
                titre = "Résumé non trouvé"

            # Rendre les scores et les résultats dans le template
            return render(request, 'sgt/proposer_travail.html', {
                'form': form,
                'resume_select': {
                    'titre': titre,
                    'resume': resume
                },
                'memoires_similaires': memoires_similaires.to_dict('records'),
                'bleu_scores': bleu_scores,
                'rouge_scores': rouge_scores
            })

    else:
        form = RechercheMemoireForm()

    return render(request, 'sgt/proposer_travail.html', {'form': form})

#Les sujets deposé
def sujet_proposer(request, sujet_id):
    sujet = get_object_or_404(SujetDeposer, id=sujet_id)
    data = {
        'sujet': sujet  
    }
    return render(request, 'sgt/sujet_detail.html', data)

#Formulaire pour deposer un sujet
def deposer_sujet(request):
    if request.method == "POST":
        form = SujetDeposerForm(request.POST)
        if form.is_valid():
            SujetDeposer = form.save()
            return redirect(home)
        else:
            # Ajoute ceci pour voir les erreurs de validation dans la console
            print(form.errors)
    else:
        form = SujetDeposerForm
    return render(request, 'sgt/deposer_sujet.html', {'form': form})

#recherche de memoire par mots clés
def rechercher_memoire(request):
    query = request.GET.get('q')  # Récupère le terme de recherche
    resultats = Memoire.objects.all()  # Initialiser avec tous les mémoires

    if query:
        mots_cles = query.split()  # Divise la requête en mots
        for mot in mots_cles:
            resultats = resultats.filter(
                Q(titre__icontains=mot) |
                #Q(resume__icontains=mot) |
                Q(key_words__icontains=mot)
            )

    return render(request, 'sgt/resultats_recherche.html', {'resultats': resultats, 'query': query})

# Dashboard étudiant
def dashboard_etudiant(request):
    # Supposons que l'utilisateur actuel est l'étudiant connecté
    #etudiant = request.user
    
    # Récupération des sujets déposés par l'étudiant
    #sujets = SujetDeposer.objects.filter(auteur=etudiant)
    
    # Récupération des interactions de l'étudiant avec son directeur ou encadreur
    #interactions = Interaction.objects.filter(etudiant=etudiant)
    
    #context = {
    #    'sujets': sujets,
    #    'interactions': interactions
    #}
    return render(request, 'sgt/dashboard_etudiant.html')



# Chargement du modèle (à exécuter une seule fois, typiquement dans  fichier d'initialisation)




# Calcul du score BLEU
def calculate_bleu(reference, hypothesis):
    reference_tokens = nltk.word_tokenize(reference.lower())  # Tokeniser le texte de référence
    hypothesis_tokens = nltk.word_tokenize(hypothesis.lower())  # Tokeniser l'hypothèse soumise

    # Le score BLEU est calculé en comparant les n-grams (groupes de mots) entre les deux textes
    bleu_score = sentence_bleu([reference_tokens], hypothesis_tokens)
    
    return bleu_score

# Calcul des scores ROUGE
def calculate_rouge(reference, hypothesis):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    
    # Comparer le résumé soumis avec le résumé de référence
    scores = scorer.score(reference, hypothesis)
    
    # Extraire les scores
    rouge1 = scores['rouge1'].fmeasure
    rouge2 = scores['rouge2'].fmeasure
    rougeL = scores['rougeL'].fmeasure
    
    return {
        'rouge1': rouge1,
        'rouge2': rouge2,
        'rougeL': rougeL
    }

# Ici je charge le modèle et les embeddings
with open('D:\DOCUMENTS\Mémoire CEDRIC L3 FTSI GI 2023-2024\sgt_ucbc\sgt_ucbc\sgt\model.pkl', 'rb') as f:
    model = pickle.load(f)

# Charge les embeddings
embeddings = np.load('D:\DOCUMENTS\Mémoire CEDRIC L3 FTSI GI 2023-2024\sgt_ucbc\sgt_ucbc\sgt\embeddings.pkl', allow_pickle=True)

# Fonction pour comparer les résumés soumis aux résumés dans la base de données
"""
@login_required
def compare(request):
    if request.method == 'POST':
        form = RechercheMemoireForm(request.POST)
        if form.is_valid():
            new_resume = form.cleaned_data['resume']  # cleaned_data pour plus de sécurité

            # embedding pour le nouveau résumé
            new_embedding = model.encode(new_resume, convert_to_tensor=True)

            # Vérifier la forme de new_embedding
            print(f"Forme de new_embedding avant ajustement: {new_embedding.shape}")
            if new_embedding.dim() == 1:
                new_embedding = new_embedding.unsqueeze(0)  # Convertir en [1, D]
            print(f"Forme de new_embedding après ajustement: {new_embedding.shape}")

            # Obtenez les embeddings existants
            embedding_values = list(embeddings.values())  # Si embeddings est un dictionnaire

            # Convertir les éléments en tenseurs
            embedding_tensors = []
            for value in embedding_values:
                if isinstance(value, dict):
                    try:
                        flat_values = [v for sublist in value.values() for v in sublist if isinstance(v, (int, float, list, np.ndarray))]
                        if flat_values:
                            tensor = torch.tensor(flat_values, dtype=torch.float32)
                            embedding_tensors.append(tensor)
                    except Exception as e:
                        print(f"Erreur lors de la conversion du dictionnaire : {e}")
                elif isinstance(value, (list, np.ndarray)):
                    try:
                        tensor = torch.tensor(value, dtype=torch.float32)
                        embedding_tensors.append(tensor)
                    except Exception as e:
                        print(f"Erreur lors de la conversion de la liste ou tableau : {e}")
                elif isinstance(value, torch.Tensor):
                    embedding_tensors.append(value)
                else:
                    print(f"Valeur non compatible ignorée : {value}")

            # Filtrer les tensors pour s'assurer qu'ils sont 1D et de même taille que new_embedding
            valid_embedding_tensors = []
            expected_dim = new_embedding.shape[1]  # Dimension D
            for tensor in embedding_tensors:
                if tensor.dim() == 2 and tensor.shape[1] == expected_dim:
                    valid_embedding_tensors.append(tensor)
                elif tensor.dim() == 1 and tensor.shape[0] == expected_dim:
                    valid_embedding_tensors.append(tensor.unsqueeze(0))  # Ajouter une dimension si nécessaire
                else:
                    print(f"Tenseur invalide ignoré: shape {tensor.shape}")

            if valid_embedding_tensors:
                # Empilez les tenseurs en un seul tenseur 2D
                embedding_tensor = torch.stack(valid_embedding_tensors)
                print(f"Forme de embedding_tensor après empilement: {embedding_tensor.shape}")

                # Vérifier si embedding_tensor est bien 2D
                if embedding_tensor.dim() != 2:
                    print("embedding_tensor n'est pas 2D")
                    # Optionnel: ajustez la forme si possible

                # Calculer les similarités cosinus
                similarities = util.pytorch_cos_sim(new_embedding, embedding_tensor)[0]
                similarities = similarities.cpu().numpy()

                # Trouver les documents les plus similaires
                top_indices = np.argsort(-similarities)[:5]
                similar_works = [memoire for idx, memoire in enumerate(Memoire.objects.all()) if idx in top_indices]
                similarity_percentages = [similarities[idx] * 100 for idx in top_indices]

                # Evaluation BLEU et ROUGE
                if similar_works:
                    reference_resume = similar_works[0].resume
                    bleu_score = calculate_bleu(reference_resume, new_resume)
                    rouge_scores = calculate_rouge(reference_resume, new_resume)
                else:
                    bleu_score = 0.0
                    rouge_scores = {'rouge1': 0.0, 'rouge2': 0.0, 'rougeL': 0.0}

                # Préparer les résultats à afficher
                results = [{
                    'Auteur': similar_works[i].auteur,
                    'Titre': similar_works[i].titre,
                    'Similarity': similarity_percentages[i]
                } for i in range(len(similar_works))]

                evaluation_results = {
                    'BLEU Score': bleu_score,
                    'ROUGE-1': rouge_scores['rouge1'],
                    'ROUGE-2': rouge_scores['rouge2'],
                    'ROUGE-L': rouge_scores['rougeL']
                }

                return render(request, 'results.html', {'cos_results': results, 'evaluation_results': evaluation_results})
    else:
        form = RechercheMemoireForm()
    return render(request, 'sgt/proposer_travail.html', {'form': form})"""
