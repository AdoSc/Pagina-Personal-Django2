from distutils.command.upload import upload
from django.db import models

# Create your models here.
# Clase del portafolio para la base de datos.
class Proyecto(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título del proyecto")
    descripcion = models.TextField(verbose_name="Descripción")
    imagen = models.ImageField(verbose_name="Imagen del proyecto", upload_to="ProyectosImagenes")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    modificado = models.DateTimeField(auto_now=True, verbose_name="Fecha de última actualización")
    
    enlace = models.URLField(null=True, blank=True, max_length=200, )
    enlace = "https://adosc.pythonanywhere.com/"

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ["-creado"]
    
    def __str__(self):
        return self.titulo
        
