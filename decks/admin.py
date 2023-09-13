from django.contrib import admin
from .models import Deck

@admin.register(Deck)
class DeckAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'imagen', 'usuario')
    search_fields = ('nombre', 'usuario__username')  # Permite buscar por nombre del mazo o nombre de usuario del creador
