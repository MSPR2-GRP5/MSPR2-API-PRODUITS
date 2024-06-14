from django.db import models

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    import_location = models.CharField(max_length=255)
    price = models.IntegerField()
    stocks = models.IntegerField()

# Create your models here.
