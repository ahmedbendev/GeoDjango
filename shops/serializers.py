from rest_framework import serializers
from .models import Shop


from rest_framework_gis.serializers import GeoFeatureModelSerializer

class ShopSerializer(GeoFeatureModelSerializer):
    """ A class to serialize locations as GeoJSON compatible data """

    class Meta:
        model = Shop
        geo_field = "point"

        # you can also explicitly declare which fields you want to include
        # as with a ModelSerializer.
         fields = ("name","shoptype","description","location","address","city",)