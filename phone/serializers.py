
from rest_framework import serializers
from .models import Phone


class Post_Phone_Serializer(serializers.ModelSerializer):
    class Meta:
        
        fields = ('id','phone_number','user_id')
        model = Phone

    # phone_number=models.IntegerField()