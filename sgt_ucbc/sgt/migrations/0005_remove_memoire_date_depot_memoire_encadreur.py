# Generated by Django 5.0.3 on 2024-09-14 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgt', '0004_memoire_directeur_memoire_annee_ac'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memoire',
            name='date_depot',
        ),
        migrations.AddField(
            model_name='memoire',
            name='Encadreur',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
