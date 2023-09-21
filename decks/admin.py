from django.contrib import admin
from .models import Deck, ShadowverseClass  # Asegúrate de importar ShadowverseClass

@admin.register(Deck)
class DeckAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'imagen', 'usuario')
    search_fields = ('nombre', 'usuario__username')  # Permite buscar por nombre del mazo o nombre de usuario del creador
    
    # Sobrescribe el método para definir los campos del formulario al crear o editar un Deck
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        
        # Recupera las opciones de clases desde el modelo ShadowverseClass
        class_choices = ShadowverseClass.objects.all().values_list('name_class', 'name_class')
        
        # Añade las opciones de clases al campo "clase_deck" en el formulario
        form.base_fields['clase_deck'].widget.choices = [('', 'Seleccionar una clase')] + list(class_choices)

        return form

# Registrar el modelo ShadowverseClass en el panel de administración
admin.site.register(ShadowverseClass)
