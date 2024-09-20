from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Faculté Profile
class FacultyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=255, verbose_name=_('Department'))
    faculty_position = models.CharField(max_length=255, verbose_name=_('Position'))
    faculty_contact_email = models.EmailField(max_length=255, verbose_name=_('Contact Email'))

    def enregistrer_enseignant(self, enseignant):
        # Logique pour enregistrer un enseignant
        pass

    def affecter_directeur(self, sujet, directeur):
        # Logique pour affecter un directeur à un sujet
        pass

    def consulter_travaux(self, travail):
        # Logique pour consulter les travaux
        pass
    
    # Faculté specific fields
    def __str__(self):
        return f'{self.user.username} Profile'

# Étudiant Profile
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=255, verbose_name=_('Student ID'))
    department = models.CharField(max_length=255, verbose_name=_('Department'))
    supervisor = models.ForeignKey('FacultyProfile', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'

# Directeur Profile
class DirectorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    faculty = models.ForeignKey(FacultyProfile, on_delete=models.SET_NULL, null=True, blank=True)
    rank = models.CharField(max_length=255, verbose_name=_('Rank'))

    def envoyer_corrections(self, travail, corrections):
        # Logique pour envoyer des corrections
        pass

    def envoyer_message_diffusion(self, message):
        # Logique pour envoyer des messages de diffusion
        pass
    
    def __str__(self):
        return f'{self.user.username} Profile'

# Encadreur Profile
class SupervisorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    director = models.ForeignKey(DirectorProfile, on_delete=models.SET_NULL, null=True, blank=True)
    
    def envoyer_corrections(self, travail, corrections):
        # Logique pour envoyer des corrections
        pass

    def __str__(self):
        return f'{self.user.username} Profile'

# Administrateur Profile
class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username} Profile'
