from django import forms
from .models import Deck, ShadowverseClass

class DeckForm(forms.ModelForm):
    clase_deck = forms.ModelChoiceField(
        queryset=ShadowverseClass.objects.all(),
        empty_label='Seleccionar una clase',
        widget=forms.RadioSelect,
        label='Clase del Mazo',
        to_field_name='name_class'  # Utilizar el nombre de la clase como valor
    )

    class Meta:
        model = Deck
        fields = ['clase_deck', 'nombre', 'descripcion', 'imagen', 'video_gameplay']
