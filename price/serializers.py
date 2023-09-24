
from rest_framework import serializers
from .models import Price


class Post_Price_Serializer(serializers.ModelSerializer):
    class Meta:
        
        fields = ('id','Price','Doctor_id')
        model = Price

# class Price(models.Model):
#     Price=models.IntegerField()