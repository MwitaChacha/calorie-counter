from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    image = models.CloudinaryField()
    email =  models.CharField(max_length=60)
    username = models.CharField(max_length=100,default='')
    def __str__(self):
        return self.user 