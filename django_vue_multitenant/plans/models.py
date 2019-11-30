from django.db import models
from django.utils.translation import ugettext_lazy as _


class Plan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    price = models.FloatField()
    custom_ingredients = models.BooleanField(verbose_name=_("Ingredientes ilimitados"), default=False)
    custom_products = models.BooleanField(verbose_name=_("Productos ilimitados"), default=False)
    is_basic = models.BooleanField(verbose_name=_("¿Es plan básico?"), default=False)

    def __str__(self):
        return self.name