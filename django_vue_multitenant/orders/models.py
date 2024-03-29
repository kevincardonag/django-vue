
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import Model
from products.models import Product
from users.models import UserProfile
from datetime import datetime


class Order(Model):
    client_name = models.CharField(max_length=100, verbose_name=_("Nombre cliente"))
    direction = models.CharField(max_length=100, verbose_name=_("Direccion cliente"))
    # email = models.EmailField(max_length=100, verbose_name=_("E-mail cliente"), null=True)
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
    
    client = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    #orderdetail = models.ManyToManyField(OrderDetail, related_name='detalleorden', verbose_name='Detalle Orden')

    @property
    def detalle(self):
        try:
            return OrderDetail.objects.filter(order=self.id)
        except OrderDetail.DoesNotExist:
            print('no hay productos')
    
    @property
    def clientObject(self):
        try:
            return UserProfile.objects.get(id=self.client_id)
        except UserProfile.DoesNotExist:
            print('no hay productos')

    # def __str__(self):
    #     return self.name


class OrderDetail(Model):
    quantity = models.IntegerField(verbose_name='Cantidad')
    price = models.FloatField(verbose_name='Costo prodocto')

    order = models.ForeignKey(Order, on_delete = models.CASCADE,related_name="products", null=True)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)

    # def __str__(self):
    #     return self.name