from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('upload', views.upload, name="upload"),
    path('image-update/<image_id>', views.image_update, name="image_update"),
    path('image-delete/<image_id>', views.image_delete, name="image_delete"),
    path('single-image/<id>', views.single_image, name="single_image"),
    path('single-image/<image_id>/comment', views.save_comment, name="save_comment"),
    path('single-image/<id>/like', views.like_image, name="like_image"),
    path('follow/<user_id>', views.follow_user, name="follow_user"),
    path('profile', views.profile, name='profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('user/<user_id>', views.user_profile, name='user_profile'),
    path('search', views.search_images, name='search')
]