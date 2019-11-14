
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import Model
from products.models import Product
from datetime import datetime

class Pedido(Model):
    client_name = models.CharField(max_length=100, verbose_name=_("Nombre cliente"))
    direction = models.CharField(max_length=100, verbose_name=_("Direccion cliente"))
    email = models.CharField(max_length=100, verbose_name=_("E-mail cliente"))
    PAYMENT_METHOD_CHOICE = (
		('contra_entrega', 'Contra Entrega'),
		('credit_cart','Tarjeta de credito'),
	)
    payment_method =  models.CharField(max_length=30,choices=PAYMENT_METHOD_CHOICE)
    price_products = models.FloatField(verbose_name='Costo')
    delivery_cost = models.FloatField(verbose_name='Costo envio')
    total = models.FloatField(verbose_name='Costo total')
    date_payment = models.DateTimeField(default=datetime.now)
    STATE_CHOICE = (
		('pedido', 'Pedido'),
		('despachado','Despachado'),
        ('entregado','Entregado'),
	)
    state =  models.CharField(max_length=22,choices=STATE_CHOICE)
    def __str__(self):
        return self.name

class PedidoDetalle(Model):
    quantity = models.IntegerField(verbose_name='Cantidad')
    price = models.FloatField(verbose_name='Costo prdocto')

    pedido = models.ForeignKey(Pedido, on_delete = models.CASCADE)
    product = models.OneToOneField(Product, on_delete = models.CASCADE)

    def __str__(self):
        return self.name
