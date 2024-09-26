from django.db import models

# Create your models here.
class ProductGroup(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    emission_low = models.FloatField()
    emission_high = models.FloatField()
    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    group = models.ForeignKey(ProductGroup, on_delete=models.DO_NOTHING)
    emission = models.FloatField()
    price = models.FloatField()
    rating = models.IntegerField()
    def __str__(self) -> str:
        return self.name + f' Group: {self.group} Rating: {self.rating}'