from django.db import models
from django.utils.translation import ugettext_lazy as _


class ActiveSwitchable(models.Model):
    """
    Behavior que agrega a un modelo las propiedades de estado activo o inactivo
    """
    is_active = models.BooleanField(default=True, verbose_name=_('Estado'))

    def switch_active(self):
        """
        Método para cambiar el estado de una notaría
        """
        self.is_active = not self.is_active
        self.save()

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    """
    Behavior que agrega a un modelo las propiedades de fecha de creación, fecha de modificación y autor de la
    modificación
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('users.UserProfile', null=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True