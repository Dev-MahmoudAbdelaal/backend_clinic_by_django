from django.db import models
from doctor.models import Doctor

# Create your models here.
class Price(models.Model):
    class PostObjects(models.Manager):
      def get_queryset(self):
          return super().get_queryset()
    id=models.AutoField(primary_key=True)
    Price=models.IntegerField()
    Doctor_id=models.ForeignKey(Doctor, on_delete=models.CASCADE,default='')

    objects = models.Manager()  # default manager
    postobjects = PostObjects()  # custom manager
