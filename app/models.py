import email
from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
# Create your models here.


class User(AbstractUser):
    full_name = models.CharField(max_length=124)
    email = models.CharField(max_length=124, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def url_formatted_name(self):
        return self.full_name.replace(' ', '+')

    @property
    def avatar(self):
        return f'https://ui-avatars.com/api/?name={self.url_formatted_name}&background=8655ff&color=fff'

# image model


class Image(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image')
    title = models.CharField(max_length=124)
    caption = models.TextField()
    like_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    # get images by user

    @classmethod
    def get_images_by_user(cls, user):
        images = cls.objects.filter(user=user)
        return images

    # save image
    def save_image(self):
        self.save()
