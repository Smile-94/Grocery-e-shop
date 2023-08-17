from django.contrib import admin

from deleveryman.models import DeleveryManInfo

# Register your models here.
@admin.register(DeleveryManInfo)
class DeleveryManInfoAdmin(admin.ModelAdmin):
    list_display = ('info_of', 'joining_date', 'employee_id', 'national_id', 'passport_no', 'driving_license', )