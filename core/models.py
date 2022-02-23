from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.
MEAL_CHOICES = (
    ('Breakfast', 'Breakfast'),
    ('Lunch', 'Lunch'),
    ('Supper', 'Supper'),
   
)


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
    serving = models.CharField(max_length=255,null=True)
    
    def __str__(self):
        return self.name 


class Profile(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    image = CloudinaryField('image',blank=True)
    email =  models.CharField(max_length=60, blank=True)
    username = models.CharField(max_length=100,default='')
    food = models.ForeignKey(Food,on_delete=models.CASCADE, related_name='foo',null=True)
    posted_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.username 


class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='eatee')
    food = models.CharField(max_length=255,null=True)
    accompaniment = models.CharField(max_length=255,null=True)
    meal = models.CharField(max_length=60, choices=MEAL_CHOICES, default="Breakfast")
    schedule_time = models.DateTimeField(null=True)
    posted_at = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name 