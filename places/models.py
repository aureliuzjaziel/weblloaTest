from django.db import models
import urllib.parse


class Place(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    subtitle = models.CharField(max_length=100, verbose_name='Subtitulo')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(upload_to='places', verbose_name='Imagen')
    url = models.URLField(blank=True, null=True, verbose_name="Enlace dirección")
    whatsapp_number = models.CharField(
        max_length=20, 
        blank=True, 
        null=True, 
        verbose_name="Número WhatsApp",
        help_text="Número con código de país (ej: 593987654321)"
    )
    menu_file = models.FileField(
        upload_to='places/menus', 
        blank=True, 
        null=True, 
        verbose_name="Menú (PDF/Imagen)",
        help_text="Sube un PDF o imagen del menú del lugar"
    )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de actualización")
    
    def get_whatsapp_url(self):
        """Genera la URL de WhatsApp con mensaje predefinido"""
        if self.whatsapp_number:
            message = f"Hola! Me interesa conocer más sobre {self.title} en Lloa."
            encoded_message = urllib.parse.quote(message)
            return f"https://wa.me/{self.whatsapp_number}?text={encoded_message}"
        return None
    
    def is_menu_image(self):
        """Verifica si el archivo del menú es una imagen"""
        if self.menu_file:
            return self.menu_file.name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))
        return False
    
    def is_menu_pdf(self):
        """Verifica si el archivo del menú es un PDF"""
        if self.menu_file:
            return self.menu_file.name.lower().endswith('.pdf')
        return False

    class Meta:
        verbose_name = "lugar"
        verbose_name_plural = "lugares"
        ordering = ["created"]
 
    def __str__(self):
        return self.title
