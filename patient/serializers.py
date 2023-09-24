
from rest_framework import serializers
from .models import Patient


class Post_patient_Serializer(serializers.ModelSerializer):
    class Meta:
        
        fields = ('id','User_ID')
        model = Patient


