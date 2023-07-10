from django.urls import path

app_name='authority'

# Authority Views
from authority.views import admin_main

urlpatterns = [
    path("authority/", admin_main.AdminView.as_view(), name="authority"),
    
]