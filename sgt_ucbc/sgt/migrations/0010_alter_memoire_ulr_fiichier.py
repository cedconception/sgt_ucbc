# Generated by Django 5.0.3 on 2024-09-15 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgt', '0009_remove_director_user_remove_memoire_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memoire',
            name='ulr_fiichier',
            field=models.URLField(blank=True),
        ),
    ]