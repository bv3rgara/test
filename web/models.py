from django.db import models


class TipoDeDocumento(models.Model):
    acronimo = models.CharField(max_length=5)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.acronimo


class Empleado(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    tipo_de_documento = models.ForeignKey(TipoDeDocumento)
    numero_de_documento = models.IntegerField(max_length=8)

    def __str__(self):
        return '{} {}'.format(self.apellido, self.nombre)
