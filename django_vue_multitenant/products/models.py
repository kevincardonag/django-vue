from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import Model


class Ingredient(Model):
    name = models.CharField(max_length=100, verbose_name=_("Nombre ingrediente"))
    price = models.IntegerField(verbose_name=_("Precio producto"))

    def __str__(self):
        return self.name

class Category(Model):
    name = models.CharField(max_length=100, verbose_name=_("Nombre de categoria"))
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    price = models.FloatField(verbose_name='Precio',null=True)
    image = models.ImageField(upload_to='products', null=True, blank=True)
    description = models.TextField(max_length=5000, verbose_name='Descripción')
    ingredient = models.ManyToManyField(Ingredient, related_name='ingredients', verbose_name='Ingredientes')
    category = models.OneToOneField(Category, on_delete = models.CASCADE, null=True)

    def __str__(self):
        return self.name

