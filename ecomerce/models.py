from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(null=True, blank=True)
    image   = models.ImageField()
    description = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.title



