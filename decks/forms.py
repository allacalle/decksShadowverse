from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Deck

class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ['nombre', 'descripcion', 'imagen', 'video_gameplay']

class ClaseDeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ['clase_deck']


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']