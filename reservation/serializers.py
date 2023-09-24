
from rest_framework import serializers
from .models import Reservation


class Post_Reservation_Serializer(serializers.ModelSerializer):
    class Meta:
        
        fields = ('id','Reservation_Number','Booking_Date', 'Patient_ID','Doctor_ID')
        model = Reservation


    # Reservation_Number=models.IntegerField()
    # Booking_Date=models.DateField(null=True)
    # Patient_ID=models.ForeignKey(Patient,on_delete=models.CASCADE,default='')
    # Doctor_ID=models.ForeignKey(Doctor,on_delete=models.CASCADE,default='')