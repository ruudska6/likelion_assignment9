from django.db import models
from django.contrib.auth.models import AbstractUser	# AbstractUser 불러오기

class User(AbstractUser):
    test = models.CharField(max_length=20, default="")
    test2 = models.CharField(max_length=20, null=True)
    first_name = None

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True)
    nickname = models.CharField(max_length=10, null = True)
    image = models.ImageField(upload_to = 'profile/', null=True)

class Meta:
    db_table = 'profile'

def __str__(self):
    return self.nickname