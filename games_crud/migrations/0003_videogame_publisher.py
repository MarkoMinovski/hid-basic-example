# Generated by Django 5.1.6 on 2025-03-05 18:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games_crud', '0002_publisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='videogame',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='games_crud.publisher'),
        ),
    ]
