# Generated by Django 4.2.16 on 2024-09-17 03:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgt', '0013_remove_sujetdeposer_bibliograph_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sujetdeposer',
            name='plan_prov',
        ),
        migrations.RemoveField(
            model_name='sujetdeposer',
            name='promotion',
        ),
        migrations.RemoveField(
            model_name='sujetdeposer',
            name='status_dir',
        ),
        migrations.RemoveField(
            model_name='sujetdeposer',
            name='status_enc',
        ),
        migrations.AlterField(
            model_name='sujetdeposer',
            name='date_prop',
            field=models.DateField(default=datetime.datetime(2024, 9, 17, 5, 0, 13, 563799)),
        ),
    ]
