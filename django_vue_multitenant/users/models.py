from django.db import models

from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.behaviors import ActiveSwitchable
from users.managers import UserProfileManager


class UserProfile(ActiveSwitchable, AbstractBaseUser, PermissionsMixin):
    """
    Modelo para los usuarios del sistema
    """
    email = models.EmailField(unique=True, verbose_name=_('Correo electrónico'))
    first_name = models.CharField(max_length=30, verbose_name=_('Nombres'))
    last_name = models.CharField(max_length=30, verbose_name=_('Apellidos'))
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='photo_user/', null=True, blank=True, verbose_name=_('Foto'))

    objects = UserManager()
    custom_objects = UserProfileManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        """
        Método para obtener el nombre completo de un usuario, requerido por AbstractBaseUser
        :return: nombres y apellidos acompañados de un espacio
        """
        full_name = '{0} {1}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Método para obtener el nombre corto de un usuario, requerido por AbstractBaseUser
        :return: nombres
        """
        return self.first_name

    def __str__(self):
        return self.get_full_name()
