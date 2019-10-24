from django.shortcuts import render
from django.contrib.auth.views import PasswordChangeView, PasswordResetView
from core.mixins import MessageMixin
from django.urls import reverse


class CustomPasswordChangeView(MessageMixin, PasswordChangeView):
    success_message = 'La contraseña se actualizó correctamente'

    def get_success_url(self):
        return reverse('login')


class CustomPasswordResetView(MessageMixin, PasswordResetView):
    success_message = 'El link para recuperar tu contraseña ha sido enviado a tu correo'

    def get_success_url(self):
        return reverse('login')

