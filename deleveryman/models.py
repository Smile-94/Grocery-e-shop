from django.db import models
import datetime

# Create your models here.
from accounts.models import User


from accounts.utils import user_directory_path



class DeleveryManInfo(models.Model):
    info_of = models.OneToOneField(User, on_delete=models.CASCADE, related_name='deleveryman_info')
    joining_date = models.DateField(auto_now_add=True)
    employee_id = models.CharField(max_length=20, unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    national_id = models.CharField(max_length=50)
    passport_no = models.CharField(max_length=50, blank=True, null=True)
    driving_license = models.CharField(max_length=50, blank=True, null=True)
    photo = models.ImageField()
    signature = models.ImageField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.employee_id:
            year = str(datetime.date.today().year)[2:4]
            month = str(datetime.date.today().month)
            day = str(datetime.date.today().day)
            self.employee_id = 'E'+year+month+day+str(self.pk).zfill(4)
            self.save()
        
    def __str__(self):
        return str(self.info_of)
