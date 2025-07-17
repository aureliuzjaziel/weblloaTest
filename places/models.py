from django.db import models
#from django.utils.timezone import now

# Create your models here.
class Place(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    subtitle = models.CharField(max_length=100, verbose_name='Subtitulo')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(upload_to='places', verbose_name='Imagen')
    #published = models.DateTimeField(
       # verbose_name="Fecha de publicación", default=now)
    url = models.URLField(blank=True, null=True, verbose_name="Enlace dirección")
       
       
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de actualización")
    
    

    class Meta:
        verbose_name = "lugar"
        verbose_name_plural = "lugares"
        ordering = ["created"]
 
    def __str__(self):
        return self.title
    # cada que se modifica el modelo se coloca migrate places
