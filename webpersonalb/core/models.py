from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="nombre")
    last_name = models.CharField(max_length=100, verbose_name="apellido")
    email = models.EmailField(verbose_name="email")
    phone = models.CharField(max_length=20, verbose_name="telefono")

    class Meta:
        verbose_name = 'contacto'
        verbose_name_plural = 'contactos'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"