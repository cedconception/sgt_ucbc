# Generated by Django 4.2.16 on 2024-09-19 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgt', '0021_alter_memoire_directeur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memoire',
            name='Directeur',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='memoire',
            name='abstract',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='memoire',
            name='auteur',
            field=models.CharField(max_length=50),
        ),
    ]