from django import forms
from .models import Memoire, SujetDeposer, Departement, Faculty, Diffusion, Correction_Travail

class RechercheMemoireForm(forms.Form):
    resume = forms.CharField(widget=forms.Textarea(attrs={'rows form-control': 4, 'placeholder': 'Entrez le résumé de travail que vous aimeriez proposer ici...'}), label='Entrez un résumé')

class MemoireForm(forms.ModelForm):
    class Meta:
        model = Memoire
        fields = ['auteur', 'titre', 'annee_ac', 'resume', 'abstract', 'Directeur', 'Encadreur', 'key_words', 'url_fichier']

class SujetDeposerForm(forms.ModelForm):
    class Meta:
        model = SujetDeposer
        fields = ['titre', 'resume', 'problematique', 'methode', 'annee_ac']
        
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
