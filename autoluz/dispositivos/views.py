from django.http import HttpResponseRedirect
from django.urls import reverse

from autoluz.dispositivos.models import Dispositivo


def update(request, id):
    dispositivos = Dispositivo.objects.get(pk=id)
    if dispositivos.status:
        dispositivos.status = False
    else:
        dispositivos.status = True
    dispositivos.save()
    ambiente_id = dispositivos.ambiente.id
    return HttpResponseRedirect(reverse('ambientes:dispositivos',  args=(ambiente_id,)))