from django.shortcuts import render
from .models import Aviso

def index(request):
    
    context = {
        'pagename': 'index'
    }
    
    return render(request, 'condominio/index.html', context)

def galery(request):
    
    context = {
        'pagename': 'galery'
    }
    
    return render(request, 'condominio/galery.html', context)

def residents(request):
    avisos = Aviso.objects.all()[:10
                                 ]
    context = {
        'pagename': 'residents',
        'avisos':avisos
    }
    
    return render(request, 'condominio/residents.html', context)

def visitors(request):
    context = {
        'pagename': 'visitors'
    }
    
    return render(request, 'condominio/visitors.html', context)