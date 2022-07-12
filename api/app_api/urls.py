from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.json_response_view , name='First View')
]