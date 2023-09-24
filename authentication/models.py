from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    id=models.AutoField(primary_key=True) 
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # def id_user(self):
    #     """
    #     Return the first_name plus the last_name, with a space in between.
    #     """
    #     return self.id_user