from django.contrib import admin
from django.urls import path
from shops import views
from .views import HomePageView,shop_datasets
urlpatterns = [
	path('', HomePageView.as_view(), name = 'home'),
]


