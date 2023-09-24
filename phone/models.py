from django.db import models
from user.models import User
#from user.models import User

# Create your models here.
class Phone(models.Model):
    class PostObjects(models.Manager):
      def get_queryset(self):
          return super().get_queryset()
    id=models.AutoField(primary_key=True)
    phone_number=models.IntegerField()
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,default='')
    objects = models.Manager()  # default manager
    postobjects = PostObjects()  # custom manager
