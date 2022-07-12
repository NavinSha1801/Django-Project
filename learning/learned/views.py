from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


from .serelizer import serializersform
from .models import index

class test_view(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self,request,*args,**kwargs):
        qs = index.objects.all()
        first = qs.first()
        serializers = serializersform(qs, many = True)   
        # serializers = serializersform(qs, many = True)
        # serializers = serializersform(first)
        return Response(serializers.data)
    def post(self,request,*args, **kwargs):
        serializer = serializersform(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

# def test_view(request):
#     data = {
#         'Name':'Navin',
#         'age':45
#     }
#     return JsonResponse(data)
