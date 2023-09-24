from django.db import models
from user.models import User
# from consulation.models import Consulation
# from reservation.models import Reservation
# Create your models here.
class Patient(models.Model):
    class PostObjects(models.Manager):
      def get_queryset(self):
          return super().get_queryset() 
    id=models.AutoField(primary_key=True)
    Upload_Photo=models.ImageField(upload_to = 'photos/%y/%m/%d',default= '')
    User_ID=models.ForeignKey(User,on_delete=models.CASCADE,default='')
    # Reservation_ID=models.ForeignKey(Reservation,on_delete=models.CASCADE,default='')
    # Consulation_ID=models.ForeignKey(Consulation,on_delete=models.CASCADE,default='')
    objects = models.Manager()  # default manager
    postobjects = PostObjects()  # custom manager