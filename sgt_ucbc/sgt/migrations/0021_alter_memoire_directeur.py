# Generated by Django 4.2.16 on 2024-09-19 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgt', '0020_memoire_cosinus_alter_memoire_directeur_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memoire',
            name='Directeur',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]