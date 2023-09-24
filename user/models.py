from django.db import models
from authentication.models import User
#from phone.models import Phone

# Create your models here.
Gender=(
   ('f','f'),
    ('m','m'),
)
type_of=(
   ('D','D'),
    ('P','P'),
)
class User(models.Model):

    class PostObjects(models.Manager):
     def upload_to (instance, filename):
             return 'images/{filename}'.format(filename=filename)
    def get_queryset(self):
          return super().get_queryset() 
    id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=64)
    gender=models.CharField(max_length=1,null=True, choices=Gender)
    Birthday=models.DateField()
    Phone=models.IntegerField(default=0)
    address_user=models.CharField(max_length=200,default='')
    # Street=models.CharField(max_length=200)
    # auth_id
    auth_id=models.ForeignKey(User,on_delete=models.CASCADE,default='', unique=True)

    User_Image=models.ImageField(upload_to = 'photos/%y/%m/%d',default= '')
    Type=models.CharField(max_length=1,null=True, choices=type_of)
    
    objects = models.Manager()  # default manager
    postobjects = PostObjects()  # custom manager