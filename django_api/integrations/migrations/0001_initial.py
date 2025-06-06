# Generated by Django 5.2 on 2025-04-16 03:17

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Inscripcion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("whatsapp", models.CharField(max_length=20)),
                ("observaciones", models.TextField(blank=True, null=True)),
                (
                    "actividad",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=20), size=None
                    ),
                ),
                ("opciones", models.JSONField()),
                ("fecha_creacion", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
