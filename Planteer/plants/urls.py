from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.all_plants, name='all_plants'),
     path('new/', views.add_plant, name='add_plant'),
]