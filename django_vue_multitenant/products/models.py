from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import Model


class Ingredient(Model):
    name = models.CharField(max_length=100, verbose_name=_("Nombre ingrediente"))
    price = models.IntegerField(verbose_name=_("Precio producto"))
