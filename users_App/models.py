from django.db import models

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