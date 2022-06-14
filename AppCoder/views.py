from django.shortcuts import render
from AppCoder.models import *

# Create your views here.
def crear_familia(request):
    lista_familia = familia.objects.all()
    return render(request, "index.html", {'lista_familia':lista_familia})

