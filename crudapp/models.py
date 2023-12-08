from django.db import models

# Create your models here.
class studentdata(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    mobile=models.IntegerField()
    mark1=models.IntegerField()
    mark2=models.IntegerField()
    mark3=models.IntegerField()
    mark4=models.IntegerField()
    

    
