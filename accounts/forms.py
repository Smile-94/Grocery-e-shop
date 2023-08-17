from django import forms
from django.contrib.auth.forms import UserCreationForm

# models
from accounts.models import User
from accounts.models import Profile

# Widgets
from accounts.widgets import CustomPictureImageFieldWidget


# forms
class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)


class ProfileForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    photo = forms.ImageField(widget=CustomPictureImageFieldWidget)
    

    class Meta:
        model = Profile
        exclude = ('user',)
