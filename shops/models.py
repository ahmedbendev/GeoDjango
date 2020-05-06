from django.db import models
from django.contrib.gis.db import models as geomodels

# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=100)
    shopimg = models.ImageField(default='default.jpg',upload_to='shop images')
    shopkeeper = models.CharField(max_length=100,default='shopkeeper')
    shoptype = models.CharField(max_length=100,default='workshop',)
    description = models.CharField(max_length=100,default='this is desriptive of the shop')
    location = geomodels.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name