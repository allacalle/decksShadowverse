from django.shortcuts import render, get_object_or_404, redirect
from .models import Deck, ShadowverseClass
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
            mazo = form.save(commit=False)
            mazo.usuario = request.user

            # Obtener el nombre de la clase seleccionada desde el formulario
            selected_class_name = form.cleaned_data['clase_deck']

            try:
                # Buscar la instancia de ShadowverseClass correspondiente al nombre seleccionado
                selected_class_instance = ShadowverseClass.objects.get(name_class=selected_class_name)

                # Asignar la instancia al campo clase_deck
                mazo.clase_deck = selected_class_instance

                mazo.save()
                print("Mazo guardado con éxito")
                return redirect('lista_decks')  # Redirige a la lista de mazos después de guardar
            except ShadowverseClass.DoesNotExist:
                print("No se encontró una instancia de clase para el nombre seleccionado:", selected_class_name)
        else:
            print(form.errors)
    else:
        form = DeckForm()

    return render(request, 'crear_deck.html', {'form': form})



class ListaDecksView(ListView):
    model = Deck
    template_name = 'lista_decks.html'
    context_object_name = 'decks'  # Nombre de la variable de contexto
    ordering = ['-fecha_publicacion']  # Ordenar por fecha de publicación, los más nuevos primero
