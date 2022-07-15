from django.shortcuts import render, HttpResponse

html_base="""
    <h1>Mi Página Personal.</h1>
    <ul>
        <li><a href="/">Portada</a></li>
        <li><a href="/Acerca/">Acerca</a></li>
        <li><a href="/Portafolio/">Portafolio</a></li>
        <li><a href="/Contacto/">Contacto</a></li>
    </ul>
"""

# Create your views here.
def Inicio(request):
    return render(request, "nucleo/Inicio.html") # Envía la dirección del código.

def Acerca(request):
    return render(request, "nucleo/Acerca.html") # Envía la dirección del código.

# La vista del protafolio que estaba aquí en la vista de la app nucleo fue movida
# a la vista de la app portafolio. 

def Contacto(request):
    return render(request, "nucleo/Contacto.html") # Envía la dirección del código.
