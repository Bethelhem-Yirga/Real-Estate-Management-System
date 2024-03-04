from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='index'),
    path('register/', views.registration_view  , name='registration'),
    path('property_listing/', views.property_listing, name='property_listing'),
    path('salespersons/', views.salespersons, name='salespersons'),
    path('contact/', views.contact, name='contact'),
    path('adminn/', views.adminn, name='adminn'),
    path('registration_view/', views.registration_view, name='registration_view'),

    path('marketing_manager/', views.properties, name='marketing_manager'),
    path('add_property/', views.add_property, name='add_property'),
    path('update_property/<int:property_id>/', views.update_property, name='update_property'),
    path('property_detail/<int:property_id>/', views.property_detail, name='property_detail'),
    path('profile_view/', views.profile_view, name='profile_view'),


    path('manager/', views.custemer, name='manager'),

    path('appform/', views.appform, name='appform'),
    path(' addemploy/', views.addemploy, name=' addemploy'),
        path(' rent/', views.rent, name='rent'),
            path('buy/', views.buy, name='buy'),


 
  
]

