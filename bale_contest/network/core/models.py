from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomeUserManager 


class CustomeUser(AbstractUser):
    username = models.CharField(max_length=32, unique=True)
    following = models.ManyToManyField('CustomeUser', related_name='followers')
    REQUIRED_FIELDS = [] 
    objects = CustomeUserManager()


class Post(models.Model):
    message = models.TextField()
    user = models.ForeignKey(CustomeUser, related_name='posts', on_delete=models.CASCADE)