from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.
MEAL_CHOICES = (
    ('Breakfast', 'Breakfast'),
    ('Lunch', 'Lunch'),
    ('Supper', 'Supper'),
   
)
class User(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    image = CloudinaryField('image')
    email =  models.CharField(max_length=60)
    username = models.CharField(max_length=100,default='')
    def __str__(self):
        return self.user 

class Food(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE, related_name='eater')
    name = models.CharField(max_length=255,null=True)
    calories = models.CharField(max_length=255,null=True)
    fat =models.CharField(max_length=255,null=True)
    sugar= models.CharField(max_length=255,null=True)
    sodium = models.CharField(max_length=255,null=True)
    protein = models.CharField(max_length=255,null=True)
    carbs = models.CharField(max_length=255,null=True)
    fibre = models.CharField(max_length=255,null=True)
    sugar = models.CharField(max_length=255,null=True)
    def __str__(self):
        return self.name 

class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='eatee')
    food = models.CharField(max_length=255,null=True)
    meal = models.CharField(max_length=60, choices=MEAL_CHOICES, default="Breakfast")
    schedule_time = models.DateTimeField(null=True)
    posted_at = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name 