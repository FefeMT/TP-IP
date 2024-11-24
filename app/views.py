# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index_page(request):
    return render(request, 'index.html')

# esta función obtiene 2 listados que corresponden a las imágenes de la API y los favoritos del usuario, y los usa para dibujar el correspondiente template.

def home(request):
    images = []
    images = services.getAllImages()
    favourite_list = []

    return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })


#Esta función muestra el html de home.html con los resultados buscados a travez de la barra de busqueda

def search(request):
    #search_msg guarda el valor de la información busacada en el buscador
    search_msg = request.POST.get('query', '')
    #images alverga la información de TODOS los personajes
    images=services.getAllImages()
     
    #este "if" se ejecuta cuando el usuario 'busca' algo en la barra del buscador, ejecutando la
    #función 'buscar' del archivo de services.py y enviando el resultado al html de home bajo el nombre de imges.
    #De no encontrar resultado muestra el mensaje "La búsqueda no arrojó resultados..." o, en caso de no rellenar la barra, redirije a 'home'.
     
    if (search_msg != ''):
        images = services.buscador(search_msg)
        return render(request, 'home.html', { 'images': images})
    else:
        return redirect('home')
    


# Estas funciones se usan cuando el usuario está logueado en la aplicación.
@login_required
def getAllFavouritesByUser(request):
    favourite_list = []
    return render(request, 'favourites.html', { 'favourite_list': favourite_list })

@login_required
def saveFavourite(request):
    pass

@login_required
def deleteFavourite(request):
    pass

@login_required
def exit(request):
    pass