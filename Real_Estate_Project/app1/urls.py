from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='index'),
    path('register/', views.registration_view  , name='registration'),
    path('property_listing/', views.property_listing, name='property_listing'),
    path('salespersons/', views.salespersons, name='salespersons'),
    path('contact/', views.contact, name='contact'),
    path('adminn/', views.adminn, name='adminn'),
    path('custemer/', views.custemer, name='custemer'),

    path('marketing_manager/', views.properties, name='marketing_manager'),
    path('manager/', views.custemer, name='manager'),

 
]

