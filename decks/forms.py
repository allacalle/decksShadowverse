# forms.py
from django import forms
from .models import Deck, ShadowverseClass

class DeckForm(forms.ModelForm):
    clase_deck = forms.ChoiceField(
        choices=[(clase.name_class, clase.name_class) for clase in ShadowverseClass.objects.all()],
        widget=forms.RadioSelect,
        label='Clase del Mazo'
    )

    class Meta:
        model = Deck
        fields = ['clase_deck', 'nombre', 'descripcion', 'imagen', 'video_gameplay']
