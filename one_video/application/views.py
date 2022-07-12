from django.http import HttpResponse
from django.shortcuts import render

from application.models import contact

# Create your views here.

def index(request):
    context = {
        'name': 'name'
    }
    return render(request, 'index.html', context)

def contacts(request):
    return render(request,'contacts.html')

def about(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        description = request.POST.get('description')
        contacts = contact(name =name, email=email, description = description)
        contacts.save()

    return render(request,'about.html')
    
