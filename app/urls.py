from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('upload', views.upload, name="upload"),
    path('single-image/<id>', views.single_image, name="single_image"),
    path('single-image/<id>/comment', views.save_comment, name="save_comment"),
]