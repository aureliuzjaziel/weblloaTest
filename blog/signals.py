from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BlogEntry
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=BlogEntry)
def enforce_blog_limit(sender, instance, created, **kwargs):
    """
    Señal que se ejecuta después de guardar una entrada del blog.
    Mantiene automáticamente el límite de 3 entradas publicadas.
    """
    # Solo procesar si la entrada está publicada
    if instance.is_published:
        try:
            # Obtener todas las entradas publicadas ordenadas por fecha
            published_entries = BlogEntry.objects.filter(
                is_published=True
            ).order_by('-published_date', '-created_date')
            
            # Si hay más de 3 entradas publicadas
            if published_entries.count() > 5:
                # Obtener las entradas que exceden el límite
                entries_to_delete = published_entries[5:]
                
                logger.info(f"Eliminando {entries_to_delete.count()} entradas del blog para mantener el límite de 3")
                
                # Eliminar las entradas más antiguas
                for entry in entries_to_delete:
                    logger.info(f"Eliminando entrada: {entry.title}")
                    
                    # Eliminar la imagen asociada si existe
                    if entry.image:
                        try:
                            entry.image.delete(save=False)
                            logger.info(f"Imagen eliminada: {entry.image.name}")
                        except Exception as e:
                            logger.error(f"Error eliminando imagen {entry.image.name}: {str(e)}")
                    
                    entry.delete()
                
                logger.info("Limpieza del blog completada exitosamente")
                
        except Exception as e:
            logger.error(f"Error en la limpieza automática del blog: {str(e)}")
