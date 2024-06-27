from django.db import models


class Products(models.Model):
    objects: models.Manager["Products"]
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()


# Create your models here.
