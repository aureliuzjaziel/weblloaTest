from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods
from .models import ContactMessage
from .forms import ContactForm
import logging

# Create your views here.
logger = logging.getLogger(__name__)

@ensure_csrf_cookie
@require_http_methods(["POST"])
def contact_submit(request):
    """
    Vista para manejar el envío del formulario de contacto via AJAX
    """
    logger.info("Contact form submission received")
    print("DEBUG: Contact form submission received")  # Debug temporal
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Guardar el mensaje en la base de datos
            contact_message = form.save()
            
            # Intentar enviar email (opcional)
            try:
                subject = f"Nuevo mensaje de contacto: {contact_message.subject}"
                message = f"""
Nuevo mensaje de contacto desde el sitio web de Turismo Lloa:

Nombre: {contact_message.name}
Email: {contact_message.email}
Asunto: {contact_message.subject}

Mensaje:
{contact_message.message}

Fecha: {contact_message.created_at.strftime('%d/%m/%Y %H:%M')}
                """
                
                # Enviar email (configura tu email en settings.py)
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    ['tu-email@ejemplo.com'],  # 🔴 CAMBIAR POR TU EMAIL
                    fail_silently=True,  # No falla si no puede enviar email
                )
            except Exception as e:
                print(f"Error enviando email: {e}")
            
            # Respuesta exitosa
            return JsonResponse({
                'success': True,
                'message': '¡Mensaje enviado exitosamente! Te contactaremos pronto.'
            })
        else:
            # Errores de validación
            return JsonResponse({
                'success': False,
                'message': 'Por favor, corrige los errores en el formulario.',
                'errors': form.errors
            })
    
    # Si no es POST, devolver error
    return JsonResponse({
        'success': False,
        'message': 'Método no permitido.'
    })
