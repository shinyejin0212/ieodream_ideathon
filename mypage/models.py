from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    # nickname = models.TextField(max_length=10,null=True)
    bio = models.TextField(max_length=20,null=True)
    profile_photo = models.ImageField(blank=True, null=True)