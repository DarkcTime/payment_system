from unicodedata import decimal
from django.db import models
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(decimal_places=2, max_digits=10000000)

    def get_description(self):
        description = self.description
        if description == '':
            return 'No description'
        return description
        