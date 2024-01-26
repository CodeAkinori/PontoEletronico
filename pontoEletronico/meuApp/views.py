from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Usuario
from django.utils import timezone
from django.http import HttpResponse

def registro(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        user_id = request.POST.get('user_id')
        
        if Usuario.objects.filter(user_id=user_id).exists():
            return HttpResponse("Usuário já existe!")

        novo_usuario = Usuario(nome=nome, user_id=user_id)
        novo_usuario.save()
        return redirect('registro')

    usuarios = Usuario.objects.all()
    return render(request, 'meuApp/registro.html', {'usuarios': usuarios})
