from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)         # Product name
    category = models.CharField(max_length=50)      # Like "Electronics", "Clothes", etc.
    price = models.FloatField()                     # Price (like 99.99)

    def __str__(self):
        return self.name
