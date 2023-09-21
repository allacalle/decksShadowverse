from django.db import models
from django.contrib.auth.models import User
import os


def custom_upload_to(instance, filename):
    return os.path.join('uploads', 'decks', filename)

class ShadowverseClass(models.Model):
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

    name_class = models.CharField(max_length=255, choices=CLASS_CHOICES, unique=True)
    icon = models.ImageField(upload_to='class_icons/')

    def __str__(self):
        return self.name_class

class Deck(models.Model):
    FORMATO_CHOICES = [
        ('Rotation', 'Rotation'),
        ('Unlimited', 'Unlimited'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to=custom_upload_to)
    video_gameplay = models.URLField(blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    wins = models.PositiveIntegerField(default=0)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    expansion_cartas = models.CharField(max_length=100, default='Desconocida')
    formato_deck = models.CharField(max_length=20, default='Rotation', choices=FORMATO_CHOICES)
    clase_deck = models.ForeignKey(ShadowverseClass, on_delete=models.SET_NULL, null=True)

class Valoracion(models.Model):
    VALORACIONES_CHOICES = [
        (1, 'Positiva'),
        (-1, 'Negativa'),
    ]
    mazo = models.ForeignKey(Deck, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    valoracion = models.IntegerField(choices=VALORACIONES_CHOICES)

    def __str__(self):
        return self.name_class
