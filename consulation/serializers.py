
from rest_framework import serializers
from .models import Consulation


class Post_Consulation_Serializer(serializers.ModelSerializer):
    class Meta:
        
        fields = ('id','Date_of_Consulation','CaseDescription', 'Medicine', 'Patient_ID','Doctor_ID')
        model = Consulation

    # Date_of_Consulation=models.DateField(null=True)
    # CaseDescription=models.CharField(max_length=256)
    # Medicine=models.CharField(max_length=256)
    # Patient_ID=models.ForeignKey(Patient,on_delete=models.CASCADE,default='')
    # Doctor_ID=models.ForeignKey(Doctor,on_delete=models.CASCADE,default='')