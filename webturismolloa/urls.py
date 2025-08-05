from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('core.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
]

# URLs de archivos media (para desarrollo y producción)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
