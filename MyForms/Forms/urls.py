from django.contrib import admin
from django.urls import path

#added manually
from . import views

urlpatterns = [
    path('', views.index , name ='Home Page')
]