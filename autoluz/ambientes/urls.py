from django.conf.urls import url

from autoluz.ambientes.views import new, dispositivos

urlpatterns = [
    url(r'^$', new, name='ambientes'),
    url(r'^(?P<id>[0-9]+)/$', dispositivos, name='dispositivos'),
]