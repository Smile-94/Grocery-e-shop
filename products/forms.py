from django import forms

# Models
from products.models import Category
from products.models import SubCategory

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        exclude = ('is_active',)


class SubCategoryForm(forms.ModelForm):

    class Meta:
        model = SubCategory
        exclude = ('is_active',)