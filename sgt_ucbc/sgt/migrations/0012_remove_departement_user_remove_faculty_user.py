# Generated by Django 4.2.16 on 2024-09-16 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sgt', '0011_memoire_key_words'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departement',
            name='user',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='user',
        ),
    ]
