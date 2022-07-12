from rest_framework import serializers

from .models import index

class serializersform(serializers.ModelSerializer):
    class Meta:
        model = index
        fields = (
            'title','description','time','owner'
        )