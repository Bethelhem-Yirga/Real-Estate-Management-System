from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='index'),
    path('register/', views.registration_view  , name='registration'),
 
]