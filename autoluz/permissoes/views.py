from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r

from autoluz.ambientes.models import Ambiente

LIST_ALUNO = ['sala_de_aula']
LIST_PROF = ['sala_de_aula', 'sala_dos_professores']
LIST_ADM = ['sala_de_aula', 'sala_dos_professores', 'corredor']

def new(request):
    ambientes = Ambiente.objects.all().order_by('-created_at')
    contenxt = []
    for ambiente in ambientes:
        ambiente = ambiente.__dict__
        #import ipdb; ipdb.set_trace()
        if request.user.groups.filter(name='aluno').exists() and ambiente['type'] in LIST_ALUNO:
            ambiente['visible'] = True
        elif request.user.groups.filter(name='professor').exists() and ambiente['type'] in LIST_PROF:
            ambiente['visible'] = True
        elif request.user.groups.filter(name='administrador').exists() and ambiente['type'] in LIST_ADM:
            ambiente['visible'] = True
        else:
            ambiente['visible'] = False
        contenxt.append(ambiente)
    return render(request, 'ambientes/ambientes-form.html', {'ambientes': contenxt})


def update(request, id):
    ambiente = Ambiente.objects.get(pk=id)
    if ambiente.status:
        ambiente.status = False
    else:
        ambiente.status = True
    ambiente.save()
    return new(request)