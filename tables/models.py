from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Language(models.Model):
    name=models.CharField(max_length=20)
    date_created=models.DateField(default=timezone.now)
    def __str__(self):
        return self.name

class Framework(models.Model):
    name=models.CharField(max_length=20)
    language=models.ForeignKey(Language,on_delete=models.CASCADE)
    date_created=models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.name
