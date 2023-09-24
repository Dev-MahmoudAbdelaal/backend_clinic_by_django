from django.db import models
from doctor.models import Doctor
from patient.models import  Patient
# Create your models here.
class Consulation(models.Model):
    class PostObjects(models.Manager):
      def get_queryset(self):
          return super().get_queryset() 
    id=models.AutoField(primary_key=True)
    Date_of_Consulation=models.DateField(null=True)
    CaseDescription=models.CharField(max_length=256)
    Medicine=models.CharField(max_length=256)
    Patient_ID=models.ForeignKey(Patient,on_delete=models.CASCADE,default='')
    Doctor_ID=models.ForeignKey(Doctor,on_delete=models.CASCADE,default='')
    objects = models.Manager()  # default manager
    postobjects = PostObjects()  # custom manager
    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = []
    def __int__(self):
        return self.id

