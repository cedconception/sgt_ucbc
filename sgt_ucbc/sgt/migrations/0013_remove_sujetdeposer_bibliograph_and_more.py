# Generated by Django 4.2.16 on 2024-09-17 02:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgt', '0012_remove_departement_user_remove_faculty_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sujetdeposer',
            name='bibliograph',
        ),
        migrations.RemoveField(
            model_name='sujetdeposer',
            name='correction',
        ),
        migrations.RemoveField(
            model_name='sujetdeposer',
            name='date_correct',
        ),
        migrations.RemoveField(
            model_name='sujetdeposer',
            name='status_dep',
        ),
        migrations.RemoveField(
            model_name='sujetdeposer',
            name='status_feu_vert',
        ),
        migrations.AlterField(
            model_name='sujetdeposer',
            name='date_prop',
            field=models.DateField(default=datetime.datetime(2024, 9, 17, 4, 45, 40, 546957)),
        ),
        migrations.AlterField(
            model_name='sujetdeposer',
            name='domaine',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='sujetdeposer',
            name='methode',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='sujetdeposer',
            name='plan_prov',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='sujetdeposer',
            name='problematique',
            field=models.TextField(blank=True),
        ),
    ]
