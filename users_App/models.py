from django.db import models
from datetime import datetime

# Create your models here.

class Profile(models.Model):
    id = models.AutoField(primary_key = True)
    user_name = models.CharField(max_length=50,null = False , blank = False)
    name = models.CharField(max_length=50,null = False,blank = False)
    email = models.EmailField(max_length = 50)
    phone = models.CharField(max_length = 10)
    profile_pic = models.ImageField(upload_to = "upload_location",null = True, blank = True)


    def __str__(self):
        return self.user_name

class User_Attendance(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    is_present = models.BooleanField(default=False)
    present_time = models.DateTimeField(default = datetime.now, blank = True)
    exit_time = models.DateTimeField(blank=True,null=True)


    def __str__(self):
        return self.user.user_name