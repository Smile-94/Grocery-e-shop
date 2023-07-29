from django.db import models
import datetime
from django.utils import timezone

# Import Validators
from common.validators import validate_float_value, validate_float_value_with_range

# Base Model
from common.models import BaseModel

class CategoryLocation(models.TextChoices):
    BODYCARE = 'bodycare', 'Bodycare'
    PRIVATE_CATE = 'private_Care', 'Private Care'
    FOOD ='food','Food'


class ProductType(models.TextChoices):
    FEATURED = 'featured', 'Featured'
    GENERAL = 'general', 'General'

    
# Create your models here.
class Category(BaseModel):
    category_name = models.CharField(max_length=50, unique=True)
    category_location = models.CharField( max_length=20, choices=CategoryLocation.choices,default=CategoryLocation.FOOD)

    def __str__(self):
        return f"{self.category_name}"
    


# Create your models here.
class SubCategory(BaseModel):
    subcategory_name = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subcategory_name}"


class Product(BaseModel):
    product_id = models.CharField(max_length=50, blank=True, null=True)
    product_name = models.CharField(max_length=200)
    product_type = models.CharField(max_length=15, choices=ProductType.choices, default='general')
    sub_catagory_1 = models.ForeignKey(SubCategory,on_delete=models.SET_NULL,related_name='categries_1',null=True,blank=True)
    sub_catagory_2 = models.ForeignKey(SubCategory,on_delete=models.SET_NULL,related_name='categries_2',null=True,blank=True)
    sub_catagory_3 = models.ForeignKey(SubCategory,on_delete=models.SET_NULL,related_name='categries_3',null=True,blank=True)
    main_image = models.ImageField(upload_to='media/product', null=True, blank=True)
    image_1 = models.ImageField(upload_to='media/product', null=True, blank=True)
    image_2 = models.ImageField(upload_to='media/product', null=True, blank=True)
    image_3 = models.ImageField(upload_to='media/product', null=True, blank=True)
    product_price = models.FloatField(null=True, blank=True, default=None, validators=[validate_float_value])
    unit = models.CharField(max_length=700, null=True, blank=True)
    stock = models.PositiveBigIntegerField(blank=False,null=False, default=0)
    discount = models.PositiveIntegerField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)


    def save(self, *args, **kwargs):
        if not self.product_id:
            current_date = datetime.date.today()
            previous_instance = Product.objects.filter(created_at__date=current_date).order_by('-created_at').first()

            if previous_instance and previous_instance.product_id:
                previous_id = previous_instance.product_id
                previous_counter = int(previous_id[-4:])  # Extract the last four digits as the counter
                new_counter = (previous_counter + 1) % 10000  # Increment and ensure it stays within four digits
            else:
                new_counter = 1

            formatted_date = current_date.strftime('%d%m%y')
            formatted_counter = str(new_counter).zfill(4)  # Ensure the counter is always four digits with leading zeros
            new_id = f'GP{formatted_date}{formatted_counter}'

            self.product_id = new_id

        super(Product, self).save(*args, **kwargs)
       
    def __str__(self):
        return f''
    
    
class ProductBatch(BaseModel):
    batch_no = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='batch_product')
    quantity = models.PositiveIntegerField(default=0)
    purchase_price = models.FloatField(null=True, blank=True, default=None, validators=[validate_float_value])
    sale_price = models.FloatField(null=True, blank=True, default=None, validators=[validate_float_value])
    mfg_date = models.DateTimeField(blank=True, null=True)
    expire_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.batch_no}-{self.product}"
    

    
    