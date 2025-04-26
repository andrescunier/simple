from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField

class Inscripcion(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20)
    observaciones = models.TextField(blank=True, null=True)
    actividad = ArrayField(models.CharField(max_length=20))
    opciones = JSONField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {', '.join(self.actividad)}"
from django.db import models

class InstagramIntegration(models.Model):
    nombre = models.CharField(max_length=100)
    token = models.TextField()
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
