from django.contrib import admin

from app.models import Follower, Image, Likes, Profile, User, Comments

# Register your models here.
admin.site.register(User)
admin.site.register(Follower)
admin.site.register(Comments)
admin.site.register(Likes)
admin.site.register(Profile)
admin.site.register(Image)
