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
    
    def save(self, *args, **kwargs):
        # Primero guardamos la instancia actual
        super().save(*args, **kwargs)
        
        # Si esta entrada se está publicando, verificamos el límite
        if self.is_published:
            self._enforce_publication_limit()
    
    def _enforce_publication_limit(self):
        """Mantiene solo las 3 entradas más recientes publicadas"""
        published_entries = BlogEntry.objects.filter(
            is_published=True
        ).order_by('-published_date', '-created_date')
        
        # Si hay más de 3 entradas publicadas
        if published_entries.count() > 5:
            # Obtener las entradas que exceden el límite
            entries_to_delete = published_entries[5:]
            
            # Eliminar las entradas más antiguas
            for entry in entries_to_delete:
                # Eliminar la imagen asociada si existe
                if entry.image:
                    entry.image.delete(save=False)
                entry.delete()
    
    @property
    def formatted_date(self):
        if self.published_date:
            return self.published_date.strftime("%d de %B de %Y")
        return self.created_date.strftime("%d de %B de %Y")
