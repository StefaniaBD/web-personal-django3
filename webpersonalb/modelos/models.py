from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    motor = models.TextField(verbose_name="Motor", max_length=200, default='Valor predeterminado')
    alimentacion = models.TextField(verbose_name="Alimentacion", max_length=200, default='Valor predeterminado')
    situacion = models.TextField(verbose_name="Situacion", default='Valor predeterminado')
    cilindraje = models.TextField(verbose_name="Cilindraje", default='Valor predeterminado')
    valvulas = models.TextField(verbose_name="Valvulas", default='Valor predeterminado')
    potencia = models.TextField(verbose_name="Potencia", default='Valor predeterminado')
    par_maximo = models.TextField(verbose_name="Par Maximo", default='Valor predeterminado')
    traccion = models.TextField(verbose_name="Traccion", default='Valor predeterminado')
    caja_de_cambios = models.TextField(verbose_name="Caja de Cambios", max_length=200, default='Valor predeterminado')
    image = models.ImageField(verbose_name="Imagen", upload_to="project")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    precio = models.TextField(verbose_name="Precio", max_length=50, default='Valor predeterminado')

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ["-created"]

    def __str__(self):
        return self.title
    