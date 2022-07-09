from django.db import models

# Create your models here.

class Proyecto(models.Model):
    titulo = models.TextField()
    status = models.TextField()