from django import forms

from autoluz.dispositivos.models import Dispositivo

class DispositivoForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Nome')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label='Senha')