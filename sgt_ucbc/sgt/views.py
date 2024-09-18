from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from .forms import MemoireForm, RechercheMemoireForm, SujetDeposerForm
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from django.contrib.auth.decorators import login_required
from .models import Memoire, SujetDeposer
import tensorflow_hub as hub
#import tensorflow as tf



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

@login_required
def ajouter_memoire(request):
    if request.method == "POST":
        form = MemoireForm(request.POST)
        if form.is_valid():
            Memoire = form.save()
            return redirect(Memoire)
        #else:
            # Ajoute ceci pour voir les erreurs de validation dans la console
            #print(form.errors)
    else:
        form = MemoireForm
    return render(request, 'sgt/ajouter_memoire.html', {'form': form})



# Je charge le modèle USE (Universal Sentence Encoder)
#embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder-multilingual/3")

@login_required
#la page de recherche du sujet de mémoire 
def proposer_memoire(request):
    form = RechercheMemoireForm()
    memoires_similaires = []
    if request.method == 'POST':
        form = RechercheMemoireForm(request.POST, request.GET)
        if form.is_valid():
            resume = form.cleaned_data['resume']
            
            # Extraire tous les résumés des mémoires depuis la base de données
            memoires = Memoire.objects.all()
            resumes = [memoire.resume for memoire in memoires]
            
            # Ajoute le résumé utilisateur dans la liste des résumés
            resumes.append(resume)
            
            # Génére des vecteurs pour tous les résumés
            vecteurs = np.embed(resumes).numpy()
            
            # Calcul de similarité entre les résumés
            sim_cos = cosine_similarity([vecteurs[-1]], vecteurs[:-1])
            indices_cos = np.argsort(-sim_cos[0])[:5]  # On récupère les 5 plus similaires
            
            # Extraire les mémoires similaires
            memoires_similaires = [memoires[i] for i in indices_cos]
            
    return render(request, 'sgt/proposer_travail.html', {'form': form, 'memoires_similaires':memoires_similaires} )

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
            return redirect(SujetDeposer)
        else:
            # Ajoute ceci pour voir les erreurs de validation dans la console
            print(form.errors)
    else:
        form = SujetDeposerForm
    return render(request, 'sgt/deposer_sujet.html', {'form': form})