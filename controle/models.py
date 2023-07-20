from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    ceated_at = models.DateTimeField(auto_now_add=True)
    
    id = models.AutoField(primary_key=True) 

    def __str__(self):
        return self.user.username
