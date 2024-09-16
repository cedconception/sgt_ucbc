from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# les roles des utilisateurs
USER_ROLES = [
    ('FAC', 'Faculté'),
    ('ETU', 'Étudiant'),
    ('DIR', 'Directeur'),
    ('ENC', 'Encadreur'),
    ('ADM', 'Administrateur'),
]
class CustomUser(AbstractUser):
    role = models.CharField(max_length=3, choices=USER_ROLES, default='ETU')

    def is_faculty(self):
        return self.role == 'FAC'

    def is_student(self):
        return self.role == 'ETU'

    def is_director(self):
        return self.role == 'DIR'

    def is_administrator(self):
        return self.role == 'ADM'

    def is_encadreur(self):
        return self.role == 'ENC'
    # Redefinir les relations pour éviter les conflits
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
    )