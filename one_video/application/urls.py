from os import abort
from django.contrib import admin
from django.urls import path

#added manually
from . import views

#added manually
admin.site.site_header = 'Navin Sharma Admin'
admin.site.site_title = 'Navin Sharma Admin Portal'
admin.site.index_title = 'Welcome to Admin Portal'

urlpatterns = [
    path('', views.index, name='Home_Page'),
    path('contacts',views.contacts, name = 'Contact_Page'),
    path('about', views.about,name = 'About Page'),
]