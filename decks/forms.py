from django import forms
from .models import Deck, ShadowverseClass

class DeckForm(forms.ModelForm):
    clase_deck = forms.ModelChoiceField(
        queryset=ShadowverseClass.objects.all(),
        empty_label='Seleccionar una clase',
        widget=forms.RadioSelect,
        label='Clase del Mazo'
    )

    class Meta:
        model = Deck
        fields = ['clase_deck', 'nombre', 'descripcion', 'imagen', 'video_gameplay']
