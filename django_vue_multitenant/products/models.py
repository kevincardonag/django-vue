from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='products', null=True, blank=True)
    description = models.TextField(max_length=5000)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name