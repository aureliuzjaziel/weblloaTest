from django.db import models
from django.utils import timezone

class BlogEntry(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    excerpt = models.TextField(max_length=300, verbose_name="Extracto", 
                              help_text="Resumen corto del artículo")
    image = models.ImageField(upload_to='blog/', verbose_name="Imagen")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")
    published_date = models.DateTimeField(blank=True, null=True, verbose_name="Fecha de publicación")
    is_published = models.BooleanField(default=False, verbose_name="Publicado")
    
    class Meta:
        verbose_name = "Entrada de Blog"
        verbose_name_plural = "Entradas de Blog"
        ordering = ['-published_date', '-created_date']
    
    def __str__(self):
        return self.title
    
    def publish(self):
        self.published_date = timezone.now()
        self.is_published = True
        self.save()
    
    @property
    def formatted_date(self):
        if self.published_date:
            return self.published_date.strftime("%d %B %Y")
        return self.created_date.strftime("%d %B %Y")
