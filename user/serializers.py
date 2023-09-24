
from rest_framework import serializers
from .models import User


class Post_User_Serializer(serializers.ModelSerializer):
    class Meta:
        
        fields = ('id','Name','gender', 'Birthday','Phone','address_user','User_Image', 'Type','auth_id')
        model = User