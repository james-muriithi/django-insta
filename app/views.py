from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
import cloudinary
import cloudinary.uploader
import cloudinary.api

from app.forms import UploadImageForm
from .models import Comments, Image, User

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
                           user_id=request.user.id)
        comment.save_comment()

        return redirect('single-image', id=image_id)
    else:
        return redirect(request.META.get('HTTP_REFERER'))
