from django.db import models

class PartidoPolitico(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre