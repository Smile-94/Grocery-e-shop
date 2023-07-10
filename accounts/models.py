from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy


# uploaded file path
from accounts.utils import user_directory_path


# Create your models here.
class MyUserManager(BaseUserManager):

    """A custom manager to deal with emails and custom identifiers"""

    def _create_user(self, email, password, **extra_fields):
        """A custom manager to deal with emails and custom identifiers"""
        if not email:
            raise ValueError('Users must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_customer(self, email, password, **extra_fields):
        user = self._create_user(email, password, **extra_fields)
        user.is_customer = True
        user.save(using=self._db)
        return user
    
    def create_deleveryman(self, email, password, **extra_fields):
        user = self._create_user(email, password, **extra_fields)
        user.is_deleveryman = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("superuser must have is_staff=True")
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have is_superuser=True')
        
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=False)
    is_customer = models.BooleanField(default=False)
    is_deleveryman=models.BooleanField(default=False)
    is_staff = models.BooleanField(
        gettext_lazy('staff_status'), default=False,
        help_text=gettext_lazy('designates whether the user can login to this site'),
    )

    is_active = models.BooleanField(
        gettext_lazy('active'), default=True,
        help_text=gettext_lazy('designates whether the user can loin to this site'),
    )

    USERNAME_FIELD = 'email'

    objects = MyUserManager()

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email


# profile models gender choices
GENDER_OPT = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other')
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=264, blank=True)
    phone_number = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=100, null=True)
    photo = models.ImageField(upload_to=user_directory_path, null=True, default='default/user.jpg')
    date_of_join = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name+"'s profile"
    
    def is_fully_filled(self):
        field_names = [f.name for f in self._meta.get_fields()]

        for field_name in field_names:
            value = getattr(self, field_name)
            if value is None or value == '':
                return False
        return True


# Abstract Base User Models
class BaseModels(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
