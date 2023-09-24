
from rest_framework import serializers
from .models import Doctor


class Post_Doctor_Serializer(serializers.ModelSerializer):
    class Meta:
        
        fields = ('id','University','Specialization','Price', 'Resume', 'User_ID')
        model = Doctor
