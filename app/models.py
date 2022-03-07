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
    REQUIRED_FIELDS = ['username', 'full_name']

    @property
    def url_formatted_name(self):
        return self.full_name.replace(' ', '+') or self.username

    @property
    def fallback_avatar(self):
        return f'https://ui-avatars.com/api/?name={self.url_formatted_name}&background=8655ff&color=fff'

    @property
    def avatar(self):
        return self.profile.avatar

    @property
    def user_following(self, append_self=True):
        following = self.followers.values_list('following__id', flat=True)
        if append_self:
            following = list(following)
            following.append(self.id)
        return following

    @classmethod
    def suggested_follows(cls, user):

        users = cls.objects.exclude(
            id__in=user.user_following).exclude(is_superuser=True)
        return users.all()

# image model


class Image(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image')
    title = models.CharField(max_length=124)
    caption = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def likes_count(self):
        return self.likes.count()

    @property
    def all_comments(self):
        return self.comments.all()

    @property
    def comments_count(self):
        return self.comments.count()

    @property
    def image_url(self):
        return self.image.build_url(format='webp')

    # get images by user
    @classmethod
    def get_images_by_user(cls, user):
        images = cls.objects.filter(user=user)
        return images

    # save image
    def save_image(self):
        self.save()

    # delete image
    def delete_image(self):
        self.delete()

    # update image caption
    def update_caption(self, caption, title):
        self.caption = caption
        self.title = title
        self.save()

    #  get a single image using id
    @classmethod
    def get_image(cls, id):
        return cls.objects.get(id=id)

    @classmethod
    def user_timeline_images(cls, user):
        images = cls.objects.filter(user__id__in=user.user_following)
        return images

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


# profile model
class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    avatar = CloudinaryField('image')
    bio = models.TextField(max_length=500, blank=True, null=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_user_profile(cls, user):
        profile = cls.objects.filter(user=user)
        return profile

    def __str__(self):
        return self.user.username


# likes model
class Likes(models.Model):
    image = models.ForeignKey(
        Image, on_delete=models.CASCADE, related_name='likes')
    vote = models.SmallIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image

    class Meta:
        verbose_name_plural = 'Likes'

# comments model


class Comments(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments")
    image = models.ForeignKey(
        Image, on_delete=models.CASCADE, related_name="comments")
    comment = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def save_comment(self):
        self.save()

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name_plural = 'Comments'
        ordering = ['-created_at']

# follower model


class Follower(models.Model):
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followers')
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.follower.full_name or self.follower.username

    class Meta:
        ordering = ['-created_at']
