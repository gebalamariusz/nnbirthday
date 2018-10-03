from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('ascii', views.ascii, name='ascii'),
    path('youtube', views.youtube, name='youtube'),
    path('map', views.map, name="map")
]