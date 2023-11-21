from django.shortcuts import render, get_object_or_404, redirect
from .models import Deck, ShadowverseClass
from .forms import DeckForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import UserRegistrationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render



def lista_decks(request):
    # Obtener todos los decks (o filtrar según tu lógica)
    all_decks = Deck.objects.order_by('-fecha_publicacion')

    # Obtener la clase seleccionada (si hay alguna)
    selected_class = request.GET.get('class')

    # Filtrar decks por la clase seleccionada
    if selected_class and selected_class != 'Todas':
        all_decks = all_decks.filter(clase_deck__name_class=selected_class)

    # Configurar la paginación con 5 decks por página
    paginator = Paginator(all_decks, 5)
    page = request.GET.get('page')

    try:
        decks = paginator.page(page)
    except PageNotAnInteger:
        # Si la página no es un número, mostrar la primera página
        decks = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango, mostrar la última página
        decks = paginator.page(paginator.num_pages)

    clases = ShadowverseClass.objects.all()

    context = {
        'decks': decks,
        'clases': clases,
        'selected_class': selected_class,
    }

    return render(request, 'lista_decks.html', context)

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


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Ruta a tu plantilla de inicio de sesión

class UserRegistrationView(CreateView):
    template_name = 'registration/register.html'  # Nombre de tu plantilla de registro
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')  # URL a la que se redirige después del registro exitoso
 