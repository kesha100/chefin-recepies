from django.db import models
from django.utils import timezone


# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=75)
    text = models.TextField()
    image = models.ImageField(upload_to='recipe/')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    

