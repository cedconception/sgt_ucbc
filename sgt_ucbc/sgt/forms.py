from django import forms

class RechercheMemoireForm(forms.Form):
    resume = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Entrez le résumé de votre travail ici...'}), label='Entrez un résumé')