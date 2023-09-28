from django import forms
from .models import Deck, ShadowverseClass

class DeckForm(forms.ModelForm):
    clase_deck = forms.ModelChoiceField(
        queryset=ShadowverseClass.objects.all(),
        empty_label=None,  # No permitir una opción vacía
        widget=forms.HiddenInput(),
    )

    class Meta:
        model = Deck
        fields = ['clase_deck', 'nombre', 'descripcion', 'imagen', 'video_gameplay']
