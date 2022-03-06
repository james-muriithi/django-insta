from django_registration.forms import RegistrationForm

from .models import User


class MyCustomUserForm(RegistrationForm):
    class Meta:
        model = User
        exclude = ()
        fields = ('username','email', 'full_name')