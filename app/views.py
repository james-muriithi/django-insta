from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
import cloudinary
import cloudinary.uploader
import cloudinary.api

from app.forms import UploadImageForm
from .models import Comments, Follower, Image, Likes, Profile, User

# Create your views here.


@login_required()
def index(request):
    images = Image.user_timeline_images(request.user)
    suggested_followers = User.suggested_follows(user=request.user)[:10]
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


@login_required
def image_update(request, image_id):
    image = Image.get_image(image_id)

    if request.method == 'POST':
        caption = request.POST['caption']
        title = request.POST['title']

        image.update_caption(caption, title)

        return redirect(request.META.get('HTTP_REFERER') or 'index')


@login_required
def image_delete(request, image_id):
    image = Image.get_image(image_id)

    image.delete_image()

    return redirect(request.META.get('HTTP_REFERER') or 'index')


@login_required()
def single_image(request, id):
    image = Image.get_image(id)
    suggested_followers = User.suggested_follows(user=request.user)[:10]
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
        following=user, follower=request.user).first()
    # check if the user has already liked the image
    if follower:
        # unlike the image
        follower.delete()

        return redirect(request.META.get('HTTP_REFERER') or 'index')
    else:
        follower = Follower(following=user, follower=request.user)
        follower.save()
        return redirect(request.META.get('HTTP_REFERER') or 'index')


@login_required()
def profile(request, user=None):
    images = user.images if user else request.user.images
    return render(request, 'profile.html', {'images': images.all()})


@login_required()
def user_profile(request, user_id):
    user = User.objects.get(username=user_id)

    images = user.images
    return render(request, 'user-profile.html', {'images': images.all(), 'usr': user})


# search for images
@login_required()
def search_images(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search').lower()
        images = Image.search_by_image_name(search_term)
        message = f'{search_term}'
        title = message

        return render(request, 'search.html', {'success': message, 'images': images})
    else:
        message = 'You havent searched for any term'
        return render(request, 'search.html', {'danger': message})


@login_required()
def update_profile(request):
    if request.method == 'POST':

        current_user = request.user

        bio = request.POST['bio']

        if request.POST['avatar']:
            profile_image = request.FILES['avatar']
            profile_image = cloudinary.uploader.upload(profile_image)
            avatar = profile_image['url']
        else:
            avatar = current_user.profile.avatar    

        # check if user exists in profile table and if not create a new profile
        if Profile.objects.filter(user_id=current_user.id).exists():

            profile = Profile.objects.get(user=current_user)
            profile.avatar = avatar
            profile.bio = bio
            profile.save()
        else:
            profile = Profile(user=current_user,
                              avatar=avatar, bio=bio)
            profile.save_profile()

    return redirect(request.META.get('HTTP_REFERER') or 'index')


# search for images
@login_required()
def search_images(request):
    if 'q' in request.GET and request.GET['q']:
        search_term = request.GET.get('q').lower()
        images = Image.search_image(search_term)

        return render(request, 'search.html', {'images': images})
    else:
        return redirect('index')