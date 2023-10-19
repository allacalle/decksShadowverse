from django.shortcuts import render, get_object_or_404, redirect
from .models import Deck, ShadowverseClass
from .forms import DeckForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView


def pagina_inicio(request):
    return render(request, 'inicio.html')


def lista_decks(request):
    decks = Deck.objects.all()
    clases = ShadowverseClass.objects.all()
    print(clases)  # Agrega esta línea para verificar si las clases se están pasando correctamente
    return render(request, 'lista_decks.html', {'decks': decks, 'clases': clases})




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

            # Obtén la opción seleccionada desde el formulario
            selected_class_name = request.POST.get('clase_deck')

            # Obtén la instancia de ShadowverseClass
            selected_class = ShadowverseClass.objects.get(name_class=selected_class_name)

            # Asigna la instancia de ShadowverseClass directamente al campo clase_deck
            mazo.clase_deck = selected_class

            mazo.save()
            print("Mazo guardado con éxito")
            return redirect('lista_decks')  # Redirige a la lista de mazos después de guardar
        else:
            print(form.errors)
    else:
        form = DeckForm()

    # Obtén todas las instancias de ShadowverseClass
    clases = ShadowverseClass.objects.all()

    return render(request, 'crear_deck.html', {'form': form, 'clases': clases})



class ListaDecksView(ListView):
    model = Deck
    template_name = 'lista_decks.html'
    context_object_name = 'decks'  # Nombre de la variable de contexto
    ordering = ['-fecha_publicacion']  # Ordenar por fecha de publicación, los más nuevos primero
