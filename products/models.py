from django.db import models
import datetime
from django.utils import timezone

# Import Validators
from common.validators import validate_float_value, validate_float_value_with_range

# Base Model
from common.models import BaseModel

class CategoryLocation(models.TextChoices):
    BARISAL = 'Barisal', 'barisal'
    CHITTAGONG = 'Chittagong', 'chittagong'
    BODYCARE = 'bodycare', 'Bodycare'
    FOOD ='food','Food'
    
# Create your models here.
class Category(BaseModel):
    category_name = models.CharField(max_length=50, unique=True)
    category_location = models.CharField( max_length=20, choices=CategoryLocation.choices,default=CategoryLocation.FOOD)


# Create your models here.
class SubCategory(BaseModel):
    subcategory_name = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Product(BaseModel):
    product_id = models.CharField(max_length=50, blank=True, null=True)
    product_name = models.CharField(max_length=200)
    sub_catagory_1 = models.ForeignKey(SubCategory,on_delete=models.SET_NULL,related_name='categries_1',null=True,blank=True)
    sub_catagory_2 = models.ForeignKey(SubCategory,on_delete=models.SET_NULL,related_name='categries_2',null=True,blank=True)
    sub_catagory_3 = models.ForeignKey(SubCategory,on_delete=models.SET_NULL,related_name='categries_3',null=True,blank=True)
    purchase_price = models.FloatField(null=True, blank=True, default=None, validators=[validate_float_value])
    image = models.ImageField(upload_to='media/product', null=True, blank=True)
    product_price = models.FloatField(null=True, blank=True, default=None, validators=[validate_float_value])
    unit = models.CharField(max_length=700, null=True, blank=True)
    stock = models.PositiveBigIntegerField(blank=False,null=False, default=0)
    discount = models.PositiveIntegerField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)


    def generate_custom_id(self):
        current_date = datetime.date.today()
        previous_instance = Product.objects.filter(created_at__date=current_date).order_by('-created_at').first()

        if previous_instance:
            previous_id = previous_instance.product_id
            previous_counter = int(previous_id[-2:])  # Extract the last two digits as the counter
            new_counter = (previous_counter + 1) % 100  # Increment and ensure it stays within two digits
        else:
            new_counter = 1

        formatted_date = current_date.strftime('%d%m%y')
        formatted_counter = str(new_counter).zfill(4)  # Ensure the counter is always two digits with leading zeros
        new_id = f'RE{formatted_date}{formatted_counter}'

        self.product_id = new_id

       
    def __str__(self):
        return self.menu_name


    
    