# Generated by Django 5.1 on 2024-09-14 15:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Correction_Travail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentaire', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Diffusion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('date_expir', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_depart', models.CharField(max_length=255)),
                ('abrev_depart', models.CharField(max_length=5)),
                ('description', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domaine_recherche', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Encadreur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domaine_recherche', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('matricule', models.CharField(max_length=50, unique=True)),
                ('mot_de_passe', models.IntegerField()),
                ('date_creation', models.DateField()),
                ('nom', models.CharField(max_length=100)),
                ('post_nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100, unique=True)),
                ('sexe', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('status', models.BooleanField(default=True)),
                ('last_msg', models.DateTimeField(blank=True, null=True)),
                ('photo_profil', models.ImageField(upload_to=None)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Memoire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentaire', models.TextField()),
                ('date_depot', models.DateTimeField()),
                ('ulr_fiichier', models.URLField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='SujetDeposer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('resume', models.TextField()),
                ('abstract', models.TextField()),
                ('problematique', models.TextField()),
                ('methode', models.TextField()),
                ('plan_prov', models.TextField()),
                ('bibliograph', models.TextField()),
                ('annee_ac', models.CharField(max_length=10)),
                ('date_prop', models.DateField()),
                ('date_correct', models.DateField(blank=True, null=True)),
                ('status_feu_vert', models.BooleanField(default=False)),
                ('status_dep', models.CharField(choices=[('non_depose', 'Non déposé'), ('depose', 'Déposé')], default='non_depose', max_length=15)),
                ('domaine', models.CharField(max_length=255)),
                ('promotion', models.CharField(max_length=255)),
                ('status_dir', models.CharField(choices=[('en_attente', 'En attente'), ('approuve', 'Approuvé'), ('rejete', 'Rejeté')], default='en_attente', max_length=15)),
                ('status_enc', models.CharField(choices=[('en_attente', 'En attente'), ('approuve', 'Approuvé'), ('rejete', 'Rejeté')], default='en_attente', max_length=15)),
                ('correction', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser')),
            ],
        ),
    ]