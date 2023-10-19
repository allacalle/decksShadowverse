from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.lista_decks, name='lista_decks'),  # URL raíz redirige a lista_decks
    path('decks/<int:deck_id>/', views.detalle_deck, name='detalle_deck'),
    path('crear_deck/', views.crear_deck, name='crear_deck'),
    # Otras URL de tu aplicación...
]

# Agrega esto al final del archivo para servir archivos de medios en modo de desarrollo.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
