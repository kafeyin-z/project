from django.contrib.auth.models import User
from django.db import models


# Create your models here.
# TODO: Kullanıcı profil modeli oluşturulacak
class UserProfile(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    career = models.CharField(null=True, blank=True, max_length=100)
    education = models.CharField(null=True, blank=True, max_length=100)
    interests = models.CharField(null=True, blank=True, max_length=100)
