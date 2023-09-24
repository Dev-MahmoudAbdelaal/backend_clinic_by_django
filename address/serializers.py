
from rest_framework import serializers
from .models import Address


class Post_Address_Serializer(serializers.ModelSerializer):
    class Meta:
        
        fields = ('id','City', 'Street','user_id')
        model = Address
