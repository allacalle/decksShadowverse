from django.db import models
from django.contrib.auth.models import User
import os

# Función personalizada para determinar la ubicación de carga de las imágenes
def custom_upload_to(instance, filename):
    # Construye la ruta relativa para almacenar la imagen dentro de la carpeta 'uploads' en la aplicación 'decks'
    return os.path.join('uploads', 'decks', filename)

class Deck(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to=custom_upload_to)  # Utiliza la función personalizada
    video_gameplay = models.URLField(blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class Valoracion(models.Model):
    VALORACIONES_CHOICES = (
        (1, 'Positiva'),
        (-1, 'Negativa'),
    )
    mazo = models.ForeignKey(Deck, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    valoracion = models.IntegerField(choices=VALORACIONES_CHOICES)
