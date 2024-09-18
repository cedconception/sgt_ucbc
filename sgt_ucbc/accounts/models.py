from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Champs communs à tous les profils
    full_name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    # Champs pour indiquer le type de profil
    role_choices = [
        ('etudiant', 'Étudiant'),
        ('directeur', 'Directeur'),
        ('encadreur', 'Encadreur'),
        ('faculte', 'Faculté'),
    ]
    role = models.CharField(max_length=50, choices=role_choices, default='etudiant')

    def __str__(self):
        return f"{self.user.username}'s profile"
    

class EtudiantProfile(Profile):
    student_id = models.CharField(max_length=50)
    field_of_study = models.CharField(max_length=100)
    year_of_study = models.IntegerField()

    def __str__(self):
        return f"Étudiant: {self.user.username}"
    
class DirecteurProfile(Profile):
    department = models.CharField(max_length=100)
    years_of_experience = models.IntegerField()

    def __str__(self):
        return f"Directeur: {self.user.username}"
    
class EncadreurProfile(Profile):
    specialisation = models.CharField(max_length=100)
    number_of_students_supervised = models.IntegerField()

    def __str__(self):
        return f"Encadreur: {self.user.username}"


