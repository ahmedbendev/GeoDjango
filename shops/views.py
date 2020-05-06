from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from .models import Shop
from django.contrib.gis.geos import Point
from django.core.serializers import serialize
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.

longitude = 3.08746
latitude = 36.7322502

user_location = Point(longitude, latitude, srid=4326)


class Home(generic.ListView):
    model = Shop
    context_object_name = 'shops'
    queryset = Shop.objects.all()
    template_name = 'index.html'


def shopsdata(request):
    if request.method== 'POST':
        city = request.POST['city']
        # if you want to add more location so the loaction filter ll work remove the line bellow this 
        city = 'all locations'
        type = request.POST['type']
        name = request.POST['name']
        if city == 'all locations':
            if type == 'all types':
                if name == 'all names':
                    shops = serialize ('geojson',Shop.objects.all(),)
                else :
                    shops = serialize ('geojson',Shop.objects.filter(name__icontains=name,)) 
            else :
                if name == 'all names':
                    shops = serialize ('geojson',Shop.objects.filter(shoptype=type,))
                else :     
                    shops = serialize ('geojson',Shop.objects.filter(name__icontains=name,shoptype=type,)) 
        else:
            if type == 'all types':
                if name == 'all names':
                    shops = serialize ('geojson',Shop.objects.filter(city=city,),)
                else :
                    shops = serialize ('geojson',Shop.objects.filter(name__icontains=name,city=city,)) 
            else :
                if name == 'all names':
                    shops = serialize ('geojson',Shop.objects.filter(shoptype=type,city=city,))
                else :     
                    shops = serialize ('geojson',Shop.objects.filter(name__icontains=name,shoptype=type,city=city,))  
        print(shops) 
        return JsonResponse(shops,content_type='json', safe=False) 
    if request.method== 'GET':    
        shops = serialize ('geojson',Shop.objects.all(),)  
        print(shops) 
        return JsonResponse(shops,content_type='json', safe=False) 


