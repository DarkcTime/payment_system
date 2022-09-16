from unicodedata import decimal
from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(decimal_places=2, max_digits=10000000)

    def get_price_dec(self):
        price_str = str(self.price).replace('.',',')
        return decimal(price_str) 