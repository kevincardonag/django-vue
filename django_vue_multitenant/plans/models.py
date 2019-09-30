from django.db import models


class Plan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    price = models.FloatField()

    def __str__(self):
        return self.name