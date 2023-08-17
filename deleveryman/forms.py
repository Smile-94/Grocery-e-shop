from django import forms

#models

from deleveryman.models import DeleveryManInfo


# Custom widgets
from deleveryman.widgets import CustomPictureImageFieldWidget
from deleveryman.widgets import CustomSignetureImageFieldWidget

class DeleveryManInfoForm(forms.ModelForm):
    employee_id = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    photo = forms.ImageField(widget=CustomPictureImageFieldWidget)
    signature = forms.ImageField(widget=CustomSignetureImageFieldWidget)

    class Meta:
        model=DeleveryManInfo
        exclude=('info_of','is_active')
