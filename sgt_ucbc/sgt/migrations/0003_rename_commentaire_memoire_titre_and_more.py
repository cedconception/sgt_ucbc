# Generated by Django 5.0.3 on 2024-09-14 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sgt', '0002_memoire_abstract_memoire_resume'),
    ]

    operations = [
        migrations.RenameField(
            model_name='memoire',
            old_name='commentaire',
            new_name='titre',
        ),
        migrations.RemoveField(
            model_name='sujetdeposer',
            name='abstract',
        ),
    ]