from django.urls import path
from . import views
from .views import payment_view



    

urlpatterns = [
    path('', views.property_listing, name='index'),
    path('register/', views.registration_view  , name='registration'),
    path('property_listing/', views.property_listing_page, name='property_listing'),
    path('salespersons/', views.salespersons, name='salespersons'),
    path('contact/', views.contact, name='contact'),
    path('adminn/', views.adminn, name='adminn'),
    path('registration_view/', views.registration_view, name='registration_view'),

    path('dashboard/', views.marketing_manager, name='marketing_manager_dashboard'),
    path('add_property/', views.add_property, name='add_property'),
    path('update_property/<int:property_id>/', views.update_property, name='update_property'),
    path('property_detail/<int:property_id>/', views.property_detail, name='property_detail'),
    path('profile_view/', views.profile_view, name='profile_view'),
    
    path('manager/', views.custemer, name='manager'),
    path('payment/', payment_view, name='payment'),
    path('appform/', views.appform, name='appform'),
    path(' addemploy/', views.addemploy, name=' addemploy'),
    path(' rent/', views.rent, name='rent'),
    path('buy/', views.buy, name='buy'),

    path('login/', views.login, name='login'),

    path('system_admin/', views.system_admin, name='system_admin'),

 
  
]

