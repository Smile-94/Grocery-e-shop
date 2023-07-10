from django.urls import path

app_name='home'

# Home Views
from home.views import home

urlpatterns = [
    path("", home.Home.as_view(), name="authority"),
    
]