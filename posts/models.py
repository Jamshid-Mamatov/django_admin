from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Posts(models.Model):
    name=models.CharField(max_length=20)
    post=models.TextField(max_length=200)
    date=models.DateField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
