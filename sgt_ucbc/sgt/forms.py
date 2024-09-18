from django import forms
from .models import Memoire, SujetDeposer, Departement, Faculty, Diffusion, Correction_Travail

class RechercheMemoireForm(forms.Form):
    resume = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Entrez le résumé de votre travail ici...'}), label='Entrez un résumé')



class MemoireForm(forms.ModelForm):
    class Meta:
        model = Memoire
        fields = ['auteur', 'titre', 'annee_ac', 'resume', 'abstract', 'Directeur', 'Encadreur', 'key_words', 'ulr_fiichier']
        widgets = {
            'auteur': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Auteur'}),
            'titre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre du mémoire'}),
            'annee_ac': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Année académique'}),
            'resume': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Résumé', 'rows': 5}),
            'abstract': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Abstract', 'rows': 5}),
            'Directeur': forms.Select(attrs={'class': 'form-control'}),
            'Encadreur': forms.Select(attrs={'class': 'form-control'}),
            'key_words': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mots-clés'}),
            'ulr_fiichier': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Lien du fichier'}),
        }
        

class SujetDeposerForm(forms.ModelForm):
    class Meta:
        model = SujetDeposer
        fields = ['titre', 'resume', 'problematique', 'methode', 'annee_ac', 'date_prop', 'domaine']
        
    def __init__(self, *args, **kwargs):
        super(SujetDeposerForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class DepartementForm(forms.ModelForm):
    class Meta:
        model = Departement
        fields = ['nom_depart', 'abrev_depart', 'description']

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['department', 'description']

class DiffusionForm(forms.ModelForm):
    class Meta:
        model = Diffusion
        fields = ['message', 'date', 'date_expir']

class Correction_TravailForm(forms.ModelForm):
    class Meta:
        model = Correction_Travail
        fields = ['commentaire', 'date']
