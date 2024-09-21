from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from django.contrib.auth.models import User


class Memoire(models.Model):
    auteur = models.CharField(max_length=50, blank=False)
    titre = models.TextField(blank=False,)
    # on s'assure que l'annee_ac is in YYYY format
    annee_ac_validator = RegexValidator(r"^\d{4}$", "Academic year must be YYYY format")
    annee_ac = models.CharField(max_length=4, default="2024", validators=[annee_ac_validator])
    #commentaire = models.TextField()
    #date_depot = models.DateTimeField()
    resume = models.TextField(blank=True)
    abstract = models.TextField(blank=True, default="") #résumé en anglais
    Directeur = models.CharField(max_length=255, blank=True, default="")
    Encadreur = models.CharField(max_length=255, blank=True)
    key_words = models.CharField(max_length=255, blank=True)
    cosinus = models.JSONField(blank=True, null=True) # stocke les indices de simularité
    
    url_fichier = models.FileField(upload_to='uploads/', blank=True)
    def __str__(self):
        return f"- {self.auteur} - {self.titre}"
    def get_absolute_url(self):
        return "/memoire/" + str(self.titre) + "/"



class SujetDeposer(models.Model):
    #auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ('en_attente', 'En attente'),
        ('approuve', 'Approuvé'),
        ('rejete', 'Rejeté'),
    ]

    STATUS_DEPOT_CHOICES = [
        ('non_depose', 'Non déposé'),
        ('depose', 'Déposé'),
    ]

    STATUS_FEUVERT_CHOICES = [
        ('accordé', 'Feu Vert Accordé'),
        ('non_accordé', 'Feu Vert Non Accordé'),
    ]

    STATUS_CORRECTION_CHOICES = [
        ('corrige', 'Corrigé'),
        ('non_corrige', 'Non Corrigé'),
    ]
    titre = models.CharField(max_length=255, blank=False)
    resume = models.TextField(blank=False)
    problematique = models.TextField(blank=True)
    methode = models.TextField(blank=True)
    #plan_prov = models.TextField(blank=True)  # Plan provisoire
    annee_ac = models.CharField(max_length=4,blank=False)  # Année académique
    date_prop = models.DateField(default=timezone.now)  # Date de proposition
    #date_correct = models.DateField(blank=True, null=True)  # Date de correction
    #status_feu_vert = models.BooleanField(default=False)  # Feu vert pour commencer
    #status_dep = models.CharField(max_length=15, choices=STATUS_DEPOT_CHOICES, default='non_depose')  # Statut du dépôt
    domaine = models.TextField(blank=True)  # Domaine de recherche
    #promotion = models.CharField(max_length=255)  # Promotion
    #status_dir = models.CharField(max_length=15, choices=STATUS_CHOICES, default='en_attente')  # Statut directeur
    #status_enc = models.CharField(max_length=15, choices=STATUS_CHOICES, default='en_attente')  # Statut encadreur
    #status_lec1 = models.CharField(max_length=15, choices=STATUS_CORRECTION_CHOICES, default='non_corrige')  # Statut lecteur 1
    #status_lec2 = models.CharField(max_length=15, choices=STATUS_CORRECTION_CHOICES, default='non_corrige')  # Statut lecteur 2
    #status_def = models.CharField(max_length=15, choices=STATUS_CHOICES, default='en_attente')  # Statut de la défense
    #correction = models.TextField(blank=True, null=True)  # Corrections proposées 
    

    def __str__(self):
        return f"{self.titre}"  
    
class Interaction(models.Model):
    etudiant = models.ForeignKey(User, on_delete=models.CASCADE)
    interlocuteur = models.CharField(max_length=255)  # Le directeur ou encadreur
    commentaire = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Etudiant(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    email = models.EmailField(max_length=255, unique=True)
    matricule = models.CharField(max_length=50, unique=True)
    date_creation = models.DateField()
    nom = models.CharField(max_length=100)
    post_nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100, unique=True)
    sexe = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15, blank=True, null=True)
    status = models.BooleanField(default=True)
    last_msg = models.DateTimeField(blank=True, null=True)
    photo_profil = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, blank=True)

    def __str__(self):
        return f"{self.nom} {self.post_nom} {self.prenom}"
    

    def proposer_sujet(self, sujet_deposer):
        # Logique pour proposer un sujet
        pass

    def deposer_travail(self, memoire):
        # Logique pour déposer un travail
        pass

class Departement(models.Model):
    nom_depart = models.CharField(max_length=255)
    abrev_depart = models.CharField(max_length=5)
    description = models.TextField(blank=True)

    def ajouter_departement(self, departement):
        pass

    def __str__(self):
        return f"{self.nom_depart}"

class Faculty(models.Model):
    ABREV_FACULTE = [
        ('FSTI', 'Faculté de Technologie et Sciences de l Ingénieur'),
        ('FSEG', 'Faculté des Sciences Economiques et de Gestion'),
    ]
    nom_fac=models.CharField(max_length=255, default="")
    department = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    def __str__(self):
        return f"{self.nom_fac}"
    

class Diffusion(models.Model):
    message = models.CharField(max_length=255)
    date = models.DateTimeField()
    date_expir = models.DateField()

class Correction_Travail(models.Model):
    commentaire = models.TextField()
    date =  models.DateField()



"""class PlagiarismCheck(models.Model):
    travail = models.ForeignKey(on_delete=models.CASCADE)
    result = models.TextField()

class MailNotification(models.Model):
    recipient = models.EmailField()
    subject = models.CharField(max_length=100)
    body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)"""