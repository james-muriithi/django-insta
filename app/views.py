from pyexpat.errors import messages
from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
import cloudinary
import cloudinary.uploader
import cloudinary.api

from app.forms import UploadImageForm
from .models import Comments, Follower, Image, Likes, User

# Create your views here.


@login_required()
def index(request):
    images = Image.user_timeline_images(request.user)
    suggested_followers = User.suggested_follows(user=request.user)
    return render(request, 'index.html', {'images': images, 'suggested_followers': suggested_followers})


@login_required()
def upload(request):
    if request.method == 'POST' and request.FILES['image']:
        form = UploadImageForm(request.POST, request.FILES)

        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()

            return redirect(request.META.get('HTTP_REFERER'), {'success': 'Image Uploaded Successfully'})

    return redirect(request.META.get('HTTP_REFERER'), {'error': 'Image Uploaded Successfully'})


@login_required()
def single_image(request, id):
    image = Image.get_image(id)
    suggested_followers = User.suggested_follows(user=request.user)
    return render(request, 'single-image.html', {'image': image, 'suggested_followers': suggested_followers})


@login_required()
def save_comment(request, image_id):
    if request.method == 'POST':
        comment = request.POST['comment']
        image = Image.objects.get(id=image_id)
        comment = Comments(comment=comment, image=image,
                           user=request.user)
        comment.save_comment()

        return redirect('single_image', id=image_id)
    else:
        return redirect(request.META.get('HTTP_REFERER') or 'index')


# like image
@login_required()
def like_image(request, id):
    like = Likes.objects.filter(image_id=id, user_id=request.user.id).first()
    # check if the user has already liked the image
    if like:
        # unlike the image
        like.delete()

        return redirect(request.META.get('HTTP_REFERER') or 'index')
    else:
        image = Image.get_image(id)
        if image and image.user.id is not request.user.id:
            like = Likes(image_id=id, user=request.user)
            like.save()
        return redirect(request.META.get('HTTP_REFERER') or 'index')

# follow user


@login_required()
def follow_user(request, user_id):
    user = User.objects.get(id=user_id)
    follower = Follower.objects.filter(
        follower=user, following=request.user).first()
    # check if the user has already liked the image
    if follower:
        # unlike the image
        follower.delete()

        return redirect(request.META.get('HTTP_REFERER') or 'index')
    else:
        follower = Follower(follower=user, following=request.user)
        follower.save()
        return redirect(request.META.get('HTTP_REFERER') or 'index')


@login_required()
def profile(request, user=None):
    return render(request, 'profile.html')