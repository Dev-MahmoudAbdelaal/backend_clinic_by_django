from django.db import models
from user.models import User
# from consulation.models import Consulation
# from reservation.models import Reservation

# Create your models here.
class Doctor(models.Model):
    class PostObjects(models.Manager):
      def get_queryset(self):
          return super().get_queryset()
    id=models.AutoField(primary_key=True) 
    University=models.CharField(max_length=200)
    Specialization=models.CharField(max_length=200)
    Price=models.IntegerField(default=0)
    #Detection_Price=models.OneToOneField(Price, on_delete=models.CASCADE)
    Resume=models.CharField(max_length=256)
    User_ID=models.ForeignKey(User,on_delete=models.CASCADE,default='')
    # Reservation_ID=models.ForeignKey(Reservation,on_delete=models.CASCADE,default='')
    # Consulation_ID=models.ForeignKey(Consulation,on_delete=models.CASCADE,default='')

    objects = models.Manager()  # default manager
    postobjects = PostObjects()  # custom manager
    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = []
    def __int__(self):
        return self.id