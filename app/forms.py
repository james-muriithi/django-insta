from django import forms
from django_registration.forms import RegistrationForm

from .models import Image, User


class MyCustomUserForm(RegistrationForm):
    class Meta:
        model = User
        fields = ('username','email', 'full_name')

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'caption', 'image')