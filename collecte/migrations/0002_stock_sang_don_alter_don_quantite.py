# Generated by Django 5.0.4 on 2024-05-05 19:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collecte', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock_sang',
            name='don',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='collecte.don'),
        ),
        migrations.AlterField(
            model_name='don',
            name='quantite',
            field=models.IntegerField(editable=False),
        ),
    ]
