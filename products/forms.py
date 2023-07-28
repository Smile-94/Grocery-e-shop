from django import forms

# Models
from products.models import Category
from products.models import SubCategory
from products.models import Product

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        exclude = ('is_active',)


class SubCategoryForm(forms.ModelForm):

    class Meta:
        model = SubCategory
        exclude = ('is_active',)


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('product_id','is_active')
    
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        # Get the queryset for sub_catagory_1
        sub_category_1_queryset = SubCategory.objects.filter(is_active=True)
        # Set the queryset for the sub_catagory_1 field
        self.fields['sub_catagory_1'].queryset = sub_category_1_queryset
        self.fields['sub_catagory_2'].queryset = sub_category_1_queryset
        self.fields['sub_catagory_3'].queryset = sub_category_1_queryset