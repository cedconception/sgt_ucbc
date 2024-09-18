from django.contrib import admin
from django.urls import include, path

from sgt import views as sgt_views

#app_name = 'sgt'

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    # Home Page: Shows a list of recent articles
    path('', sgt_views.home, name='home'),

    #about
    path('about/', sgt_views.about, name='about'),
    
    #memoire detail
    path('memoire/<int:memoire_id>/', sgt_views.memoire_detail, name='memoire_detail'),
    path('memoire/ajouter/', sgt_views.ajouter_memoire, name='ajouter_memoire'),

    #proposition de sujet recommandation et recherche de similaires mémoires
    path('propose/', sgt_views.proposer_memoire, name='proposer_memoire'),

    #depot de sujet mémoires
    path('sujet/<int:sujet_id>/', sgt_views.sujet_proposer, name='sujet_proposer'),
    path('sujet/deposer_sujet/', sgt_views.deposer_sujet, name='deposer_sujet'),
    

    
]