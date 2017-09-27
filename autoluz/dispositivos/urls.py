from django.conf.urls import url

from autoluz.dispositivos.views import update

urlpatterns = [
    url(r'^(?P<id>[0-9]+)/$', update, name='update'),
]