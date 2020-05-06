from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from shops import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view()),
    path('shopsdata/', views.shopsdata , name='shopsdata'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)