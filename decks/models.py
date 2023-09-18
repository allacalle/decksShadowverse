from django.db import models
from django.contrib.auth.models import User
import os

# Función personalizada para determinar la ubicación de carga de las imágenes
def custom_upload_to(instance, filename):
    # Construye la ruta relativa para almacenar la imagen dentro de la carpeta 'uploads' en la aplicación 'decks'
    return os.path.join('uploads', 'decks', filename)

class ShadowverseClass(models.Model):
    # Define los nombres de las clases en inglés
    CLASS_CHOICES = [
        ('Forestcraft', 'Forestcraft'),
        ('Swordcraft', 'Swordcraft'),
        ('Runecraft', 'Runecraft'),
        ('Dragoncraft', 'Dragoncraft'),
        ('Shadowcraft', 'Shadowcraft'),
        ('Bloodcraft', 'Bloodcraft'),
        ('Havencraft', 'Havencraft'),
        ('Portalcraft', 'Portalcraft'),
    ]

    # Campo para el nombre de la clase
    name_class = models.CharField(max_length=255, choices=CLASS_CHOICES, unique=True)

    # Campo para el icono único de la clase (puedes usar ImageField para el icono)
    icon = models.ImageField(upload_to='class_icons/')



class Deck(models.Model):
        # Agrega esta definición de opciones para el campo 'formato_mazo'
    FORMATO_CHOICES = [
        ('Rotation', 'Rotation'),
        ('Unlimited', 'Unlimited'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to=custom_upload_to)  # Utiliza la función personalizada
    video_gameplay = models.URLField(blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Nuevos campos con valores por defecto
    wins = models.PositiveIntegerField(default=0)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    expansion_cartas = models.CharField(max_length=100, default='Desconocida')
    formato_mazo = models.CharField(max_length=20, default='Rotation', choices=FORMATO_CHOICES)



class Valoracion(models.Model):
    VALORACIONES_CHOICES = (
        (1, 'Positiva'),
        (-1, 'Negativa'),
    )
    mazo = models.ForeignKey(Deck, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    valoracion = models.IntegerField(choices=VALORACIONES_CHOICES)

    def __str__(self):
        return self.name_class
