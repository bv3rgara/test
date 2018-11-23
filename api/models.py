from django.db import models


class TipoDeDocumento(models.Model):
    descripcion = models.CharField(max_length=30)

    def __str__(self):
        return self.descripcion


class Empleado(models.Model):
    tipo_de_documento = models.ForeignKey(TipoDeDocumento)
    numero_de_documento = models.IntegerField()
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)

    def __str__(self):
        return '{} {}'.format(self.apellido, self.nombre)
