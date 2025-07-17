from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
    verbose_name = 'Blog de Turismo'
    
    def ready(self):
        """Importar las señales cuando la app esté lista"""
        import blog.signals
