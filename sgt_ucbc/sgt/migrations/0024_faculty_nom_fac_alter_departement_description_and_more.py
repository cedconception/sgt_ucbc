# Generated by Django 4.2.16 on 2024-09-21 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgt', '0023_alter_sujetdeposer_annee_ac'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='nom_fac',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='departement',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]