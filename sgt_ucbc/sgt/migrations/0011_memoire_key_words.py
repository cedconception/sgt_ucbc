# Generated by Django 5.0.3 on 2024-09-15 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgt', '0010_alter_memoire_ulr_fiichier'),
    ]

    operations = [
        migrations.AddField(
            model_name='memoire',
            name='key_words',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
