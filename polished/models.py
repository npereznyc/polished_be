from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Polish(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='polishes')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['brand', 'name']

class User(models.Model):
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    polish = models.ForeignKey(Polish, on_delete=models.PROTECT, related_name='reviews')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='reviews')
    image =  models.TextField()
    review =  models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['created_at']


    def __str__(self):
        return self.review

class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')

    def __str__(self):
        return self.user

