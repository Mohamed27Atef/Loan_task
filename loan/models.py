from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class loan(models.Model):
     amount=models.IntegerField(null=True,blank=True)
     Term_of_Loan=models.IntegerField(null=True,blank=True)
     Annual_Interest_Rate=models.FloatField(null=True,blank=True)
     Compound_Periods=models.IntegerField(null=True,blank=True)
     Payments_Per_Year=models.IntegerField(null=True,blank=True)

     date=models.DateTimeField(default=timezone.now)
     author=models.ForeignKey(User,on_delete=models.CASCADE)     
       #  return self.name