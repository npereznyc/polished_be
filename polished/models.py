from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Polish(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='polishes')

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    polish = models.ForeignKey(Polish, on_delete=models.CASCADE, related_name='reviews')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='reviews')
    image =  models.TextField()
    review =  models.TextField()

    def __str__(self):
        return self.review

class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')

    def __str__(self):
        return self.user