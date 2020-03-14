from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Member(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     phone = models.CharField(max_length=50)
     address = models.CharField(max_length=150)
     
     
     

    
