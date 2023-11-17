from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.

class StreamPlateform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)
    
    def __str__(self):
        return self.name
    
class WatchList(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True) #is released or launched
    created = models.DateTimeField(auto_now_add=True)
    avg_rating = models.FloatField(default=0)
    number_rating = models.IntegerField(default=0)
    
    plateform = models.ForeignKey(StreamPlateform, on_delete=models.CASCADE, related_name="watchlist")
    
    
    def __str__(self):
        return self.title

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="reviews")
    
    def __str__(self):
        return str(self.rating) + " | " + self.watchlist.title + " | " + str(self.author)