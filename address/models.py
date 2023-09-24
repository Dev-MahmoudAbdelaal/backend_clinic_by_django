from django.db import models
from user.models import User


# Create your models here.
class Address(models.Model):
    class PostObjects(models.Manager):
      def get_queryset(self):
          return super().get_queryset() 
    id=models.AutoField(primary_key=True)
    City=models.CharField(max_length=200)
    Street=models.CharField(max_length=200)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,default='')

    objects = models.Manager()  # default manager
    postobjects = PostObjects()  # custom manager

