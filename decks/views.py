from django.shortcuts import render, get_object_or_404
from .models import Deck

def pagina_inicio(request):
    return render(request, 'inicio.html')

def lista_decks(request):
    decks = Deck.objects.all()
    return render(request, 'lista_decks.html', {'decks': decks})

def detalle_deck(request, deck_id):
    deck = get_object_or_404(Deck, pk=deck_id)
    return render(request, 'detalle_deck.html', {'deck': deck})

