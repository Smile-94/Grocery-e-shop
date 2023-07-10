from django.contrib import admin

# models
from accounts.models import User
from accounts.models import Profile

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('email','is_customer','is_deleveryman','is_staff','is_active')
    search_fields=('email',)
    list_filter=('email','is_customer','is_deleveryman')
    list_per_page=50

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','full_name','date_of_join')
    search_fields=('user','first_name','date_of_join')
    list_filter=('date_of_join',)
    aw_id_fields=('user',)
    list_per_page=50





