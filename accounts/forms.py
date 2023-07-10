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
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    address_1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Address 1'}))
    address_2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Address 2'}))
    photo = forms.ImageField(widget=CustomPictureImageFieldWidget)

    class Meta:
        model = Profile
        exclude = ('user',)
