from django import forms
from .models import Deck, ShadowverseClass

class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ['nombre', 'descripcion', 'imagen', 'video_gameplay']
