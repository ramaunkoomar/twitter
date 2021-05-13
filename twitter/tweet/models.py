from django.db import models
from cloudinary.models import CloudinaryField
from django.utils import timezone
# Create your models here.

class tweet(models.Model):
    name=models.CharField(max_length=20,default='blank')
    username=models.CharField(max_length=20,default='blank')
    tweet_at=models.DateTimeField(auto_now=timezone.now)
    profile_img=models.FileField(upload_to='profile/user',default='blank')
    tweet_text=models.CharField(max_length=255,default='blank')
    tweet_img=models.FileField(upload_to='tweet',default='blank')
    like=models.IntegerField(default=0)