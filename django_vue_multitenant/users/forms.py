from django import forms
from django.contrib.auth.models import User, Group
from users.models import UserProfile
from parsley.decorators import parsleyfy


@parsleyfy
class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirmación de contraseña")
    group = forms.ModelChoiceField(Group.objects.all(), label="Grupo")

    class Meta:
        parsley_extras = {
            'password': {
                'minlength': "5",
            },
            'password_confirm': {
                'equalto': "password",
                'error-message': "Las contraseñas ingresadas no son iguales",
            },
        }
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Email',
        }
        model = UserProfile
        fields = ('first_name', 'last_name', 'email')

@parsleyfy
class UserClientForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirmación de contraseña")
    

    class Meta:
        parsley_extras = {
            'password': {
                'minlength': "5",
            },
            'password_confirm': {
                'equalto': "password",
                'error-message': "Las contraseñas ingresadas no son iguales",
            },
        }
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Email',
        }
        model = UserProfile
        fields = ('first_name', 'last_name', 'email')