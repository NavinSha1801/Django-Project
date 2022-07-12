from django.shortcuts import render

#added manually
from django.http import JsonResponse

# Create your views here.
def json_response_view(request):
    data = {
        'status':200,
        'description':'OK'
    }
    return JsonResponse(data='data')