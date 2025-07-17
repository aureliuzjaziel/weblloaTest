from django.core.management.base import BaseCommand
from blog.models import BlogEntry
import os

class Command(BaseCommand):
    help = 'Limpia las entradas del blog manteniendo solo las 3 más recientes publicadas'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Muestra qué entradas se eliminarían sin eliminarlas realmente',
        )
        parser.add_argument(
            '--limit',
            type=int,
            default=5,
            help='Número máximo de entradas publicadas a mantener (por defecto: 3)',
        )

    def handle(self, *args, **options):
        limit = options['limit']
        dry_run = options['dry_run']
        
        # Obtener todas las entradas publicadas ordenadas por fecha
        published_entries = BlogEntry.objects.filter(
            is_published=True
        ).order_by('-published_date', '-created_date')
        
        total_published = published_entries.count()
        
        self.stdout.write(
            self.style.SUCCESS(f'Entradas publicadas encontradas: {total_published}')
        )
        
        if total_published <= limit:
            self.stdout.write(
                self.style.SUCCESS(f'No hay entradas que eliminar. Límite: {limit}')
            )
            return
        
        # Obtener las entradas que exceden el límite
        entries_to_delete = published_entries[limit:]
        entries_count_to_delete = entries_to_delete.count()
        
        self.stdout.write(
            self.style.WARNING(f'Entradas a eliminar: {entries_count_to_delete}')
        )
        
        # Mostrar las entradas que se van a eliminar
        for entry in entries_to_delete:
            date_str = entry.formatted_date
            self.stdout.write(f'  - "{entry.title}" (publicada: {date_str})')
        
        if dry_run:
            self.stdout.write(
                self.style.WARNING('Modo de prueba activado. No se eliminó ninguna entrada.')
            )
            return
        
        # Confirmar eliminación
        confirm = input(f'\n¿Estás seguro de eliminar {entries_count_to_delete} entradas? (sí/no): ')
        if confirm.lower() not in ['sí', 'si', 'yes', 'y']:
            self.stdout.write(self.style.ERROR('Operación cancelada.'))
            return
        
        # Eliminar las entradas
        deleted_count = 0
        for entry in entries_to_delete:
            try:
                # Eliminar la imagen asociada si existe
                if entry.image:
                    if os.path.exists(entry.image.path):
                        os.remove(entry.image.path)
                        self.stdout.write(f'    Imagen eliminada: {entry.image.name}')
                
                entry.delete()
                deleted_count += 1
                self.stdout.write(f'  ✓ Eliminada: "{entry.title}"')
                
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'  ✗ Error eliminando "{entry.title}": {str(e)}')
                )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'\nProceso completado. Eliminadas: {deleted_count}/{entries_count_to_delete} entradas.'
            )
        )
        
        # Mostrar el estado final
        final_count = BlogEntry.objects.filter(is_published=True).count()
        self.stdout.write(
            self.style.SUCCESS(f'Entradas publicadas actuales: {final_count}/{limit}')
        )
