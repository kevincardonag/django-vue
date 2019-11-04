from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import Model


class Ingredient(Model):
    name = models.CharField(max_length=100, verbose_name=_("Nombre ingrediente"))
    price = models.IntegerField(verbose_name=_("Precio producto"))


class Product(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='products', null=True, blank=True)
    description = models.TextField(max_length=5000)
    stock = models.IntegerField(default=0)
    ingredient = models.ManyToManyField(Ingredient, related_name='ingredients')

    def __str__(self):
        return self.name

