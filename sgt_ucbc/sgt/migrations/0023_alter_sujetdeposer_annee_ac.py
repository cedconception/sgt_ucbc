# Generated by Django 4.2.16 on 2024-09-20 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgt', '0022_alter_memoire_directeur_alter_memoire_abstract_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sujetdeposer',
            name='annee_ac',
            field=models.CharField(max_length=4),
        ),
    ]