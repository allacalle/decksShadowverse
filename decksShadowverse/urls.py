from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('decks.urls')),  # Incluye las URL de tu aplicación 'decks'
]

# Agrega esto al final del archivo para servir archivos de medios en modo de desarrollo.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

