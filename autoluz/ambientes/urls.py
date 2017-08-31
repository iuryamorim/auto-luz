from django.conf.urls import url

from autoluz.ambientes.views import new, update

urlpatterns = [
    url(r'^$', new, name='ambientes'),
    url(r'^(?P<id>[0-9]+)/$', update, name='update'),
]