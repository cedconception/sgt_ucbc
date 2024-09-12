from django.shortcuts import render

def home(request):
    return render(request, 'sgt/home.html')


def memoire_detail(request):
    return render(request, 'sgt/memoire_detail.html')

def proposer_memoire(request):
    return render(request, 'sgt/proposer_travail.html')

#depot de sujet mémoires
def deposer_sujet(request):
    return render(request, 'sgt/deposer_sujet.html')