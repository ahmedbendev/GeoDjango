from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from .models import Shop
from django.contrib.gis.geos import Point
# Create your views here.

longitude = 3.08746
latitude = 36.7322502

user_location = Point(longitude, latitude, srid=4326)


class Home(generic.ListView):
    model = Shop
    context_object_name = 'shops'
    queryset = Shop.objects.annotate(distance=Distance('location',
    user_location)
    ).order_by('distance')[0:6]
    template_name = 'index.html'