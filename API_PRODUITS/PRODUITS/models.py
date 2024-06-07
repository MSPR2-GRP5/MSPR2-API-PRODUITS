from django.db import models

class products(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    import_location = models.CharField(max_length=60)
    price = models.IntegerField()
    stocks = models.IntegerField()




# Create your models here.
