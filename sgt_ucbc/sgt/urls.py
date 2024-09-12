from django.contrib import admin
from django.urls import path

from sgt import views as sgt_views

#app_name = 'sgt'

urlpatterns = [
    # Home Page: Shows a list of recent articles
    path('', sgt_views.home, name='home'),
    
    #memoire detail
    path('memoire/', sgt_views.memoire_detail, name='memoire_detail'),

    #proposition de sujet recommandation et recherche de similaires mémoires
    path('propose/', sgt_views.proposer_memoire, name='proposer_memoire'),

    #depot de sujet mémoires
    path('deposer_sujet/', sgt_views.deposer_sujet, name='deposer_sujet'),
    

    
]