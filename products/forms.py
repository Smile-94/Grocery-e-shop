from django import forms

# Models
from products.models import Category
from products.models import SubCategory
from products.models import Product
from products.models import Order

# Import Widgets
from products.widgets import CustomPictureImageFieldWidget

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        exclude = ('is_active',)


class SubCategoryForm(forms.ModelForm):

    class Meta:
        model = SubCategory
        exclude = ('is_active',)


class ProductForm(forms.ModelForm):

    main_image = forms.ImageField(widget=CustomPictureImageFieldWidget)
    image_1 = forms.ImageField(widget=CustomPictureImageFieldWidget)
    image_2 = forms.ImageField(widget=CustomPictureImageFieldWidget)
    image_3 = forms.ImageField(widget=CustomPictureImageFieldWidget)

    class Meta:
        model = Product
        exclude = ('product_id', 'product_type','is_active')
    
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        # Get the queryset for sub_catagory_1
        sub_category_1_queryset = SubCategory.objects.filter(is_active=True)
        # Set the queryset for the sub_catagory_1 field
        self.fields['sub_catagory_1'].queryset = sub_category_1_queryset
        self.fields['sub_catagory_2'].queryset = sub_category_1_queryset
        self.fields['sub_catagory_3'].queryset = sub_category_1_queryset

class OrderConfirmForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('order_confirm', 'assigned_to')