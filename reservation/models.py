from django.db import models
from doctor.models import Doctor
from patient.models import  Patient

# Create your models here.
class Reservation(models.Model):
    class PostObjects(models.Manager):
      def get_queryset(self):
          return super().get_queryset() 
    id=models.AutoField(primary_key=True)
    Reservation_Number=models.IntegerField()
    Booking_Date=models.DateField(null=True)
    Patient_ID=models.ForeignKey(Patient,on_delete=models.CASCADE,default='')
    Doctor_ID=models.ForeignKey(Doctor,on_delete=models.CASCADE,default='')
    objects = models.Manager()  # default manager
    postobjects = PostObjects()  # custom manager