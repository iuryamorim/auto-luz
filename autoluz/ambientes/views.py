from django.shortcuts import render

from autoluz.dispositivos.models import Dispositivo
from autoluz.ambientes.models import Ambiente
from autoluz.permissoes.models import Permissoes


def new(request):
    ambientes = Ambiente.objects.all().order_by('-created_at')
    return render(request, 'ambientes/ambientes-form.html', {'ambientes': ambientes})


def dispositivos(request, id):
    dispositivos = Dispositivo.objects.filter(ambiente__pk=id)
    permissoes = Permissoes.objects.filter(usuario__pk=request.user.pk)
    dispositivos_ids = [permissao.dispositivo.id for permissao in permissoes]
    disp = []
    for dispositivo in dispositivos:
        dispositivo = dispositivo.__dict__
        if dispositivo["id"] in dispositivos_ids:
            dispositivo["permission"] = True
        else:
            dispositivo["permission"] = False
        disp.append(dispositivo)

    return render(request, 'ambientes/ambientes-dispositivos.html', {'dispositivos': disp})
