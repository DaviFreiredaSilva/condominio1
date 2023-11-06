import os
from django.shortcuts import render, redirect
from .models import Aviso

def index(request):
    
    context = {
        'pagename': 'index'
    }
    
    return render(request, 'condominio/index.html', context)

def residents(request):
    avisos = Aviso.objects.all()[:10]
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

def config(request):
    context = {
        'pagename': 'config'
    }

    return render(request, 'condominio/config.html', context)

def avisoManage(request):
    avisos = Aviso.objects.all()[:10]

    if request.method == 'POST':
        titulo = request.POST['titulo']
        imagem = request.FILES['imagem']
        texto = request.POST['texto']

        aviso = Aviso(
            titulo = titulo,
            imagem=imagem,
            texto=texto
        )
        aviso.save()
        return redirect('residents')
    context = {
        'avisos':avisos
    }

    return render(request, 'condominio/aviso-manage.html', context)

def avisoDetails(request, id):
    aviso = Aviso.objects.get(id=id)
    context = {
        'aviso':aviso
    }

    return render(request, 'condominio/aviso-details.html', context)

def avisoEdit(request, id):
    aviso = Aviso.objects.get(id=id)
    context = {
        'aviso':aviso
    }

    return render(request, 'condominio/aviso-edit.html', context)

def avisoDelete(request, id):
    aviso = Aviso.objects.get(id=id)
    if aviso is not None:
        os.remove('media/'+str(aviso.imagem))
        aviso.delete()
    
    return redirect('residents')