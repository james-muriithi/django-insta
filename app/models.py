from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
# Create your models here.

class User(AbstractUser):
    full_name = models.CharField(max_length=124)

# image model
class Image(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image')
    title = models.CharField(max_length=124)
    caption = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)