from django.urls import path


app_name = 'deleveryman'

#Import Views
from deleveryman.views import DeleveryManHomeView


urlpatterns = [

path('deleveryman/', DeleveryManHomeView.as_view(), name='deleveryman'),
   
]