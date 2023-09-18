from django.shortcuts import render, get_object_or_404, redirect
from .models import Deck
from .forms import DeckForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

def pagina_inicio(request):
    return render(request, 'inicio.html')

def lista_decks(request):
    decks = Deck.objects.all()
    return render(request, 'lista_decks.html', {'decks': decks})

def detalle_deck(request, deck_id):
    deck = get_object_or_404(Deck, pk=deck_id)
    return render(request, 'detalle_deck.html', {'deck': deck})

@login_required
def crear_deck(request):
    if request.method == 'POST':
        form = DeckForm(request.POST, request.FILES)
        if form.is_valid():
            # Guarda el mazo en la base de datos
            mazo = form.save(commit=False)
            mazo.usuario = request.user  # Asigna el usuario actual como propietario del mazo
            mazo.save()
            return redirect('lista_decks')  # Redirige a la lista de mazos
    else:
        form = DeckForm()
    
    return render(request, 'crear_deck.html', {'form': form})

class ListaDecksView(ListView):
    model = Deck
    template_name = 'lista_decks.html'
    context_object_name = 'decks'  # Nombre de la variable de contexto
    ordering = ['-fecha_publicacion']  # Ordenar por fecha de publicación, los más nuevos primero
