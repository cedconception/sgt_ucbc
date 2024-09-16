from django.shortcuts import render

from .forms import RechercheMemoireForm
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from .models import Memoire
#import tensorflow_hub as hub
#import tensorflow as tf



def home(request):
    memoires = Memoire.objects.all()
    #memoires = (Memoire.objects.filter(is_published=True) .order_by('-pub_date')[:10])
    data={
        'memoires':memoires
    }
    return render(request, 'sgt/home.html', data)


def memoire_detail(request, memoire_id):
    memoire = Memoire.objects.get(id=memoire_id)
    data = {
        'memoire': memoire
    }
    return render(request, 'sgt/memoire_detail.html', data)

# Je charge le modèle USE (Universal Sentence Encoder)
#embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder-multilingual/3")

#la page de recherche du sujet de mémoire 
def proposer_memoire(request):
    """form = RechercheMemoireForm()
    memoires_similaires = []
    if request.method == 'POST':
        form = RechercheMemoireForm(request.POST)
        if form.is_valid():
            resume = form.cleaned_data['resume']
            
            # Extraire tous les résumés des mémoires depuis la base de données
            memoires = Memoire.objects.all()
            resumes = [memoire.resume for memoire in memoires]
            
            # Ajoute le résumé utilisateur dans la liste des résumés
            resumes.append(resume)
            
            # Génére des vecteurs pour tous les résumés
            vecteurs = embed(resumes).numpy()
            
            # Calcul de similarité entre les résumés
            sim_cos = cosine_similarity([vecteurs[-1]], vecteurs[:-1])
            indices_cos = np.argsort(-sim_cos[0])[:5]  # On récupère les 5 plus similaires
            
            # Extraire les mémoires similaires
            memoires_similaires = [memoires[i] for i in indices_cos]"""
    return render(request, 'sgt/proposer_travail.html')

#depot de sujet mémoires
def deposer_sujet(request):
    return render(request, 'sgt/deposer_sujet.html')