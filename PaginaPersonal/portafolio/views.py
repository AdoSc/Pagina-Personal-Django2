from django.shortcuts import render
from .models import Proyecto

# Create your views here.
def Portafolio(request):
    proyectosweb = Proyecto.objects.all()
    return render(request, "portafolio/Portafolio.html", {'proyectosweb': proyectosweb}) # Envía la dirección del código.
    