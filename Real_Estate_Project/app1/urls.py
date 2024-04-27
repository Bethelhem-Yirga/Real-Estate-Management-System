from django.urls import path
from . import views
from .views import change_password
from .views import contact_view, payment_view, add_employee, update_employee_active_status, accept_or_reject_application
from .views import finance_form, success_page
from django.urls import path
from .views import finance_with_property_data
urlpatterns = [
    path('', views.property_listing, name='index'),
    path('register/', views.registration_view, name='registration'),
    path('property_listing/', views.property_listing_page, name='property_listing'),
    path('salespersons/', views.salespersons, name='salespersons'),
    path('contact/', views.contact, name='contact'),
    path('accept/<int:application_id>/', accept_or_reject_application, {'decision': 'accept'}, name='accept_application'),
    path('reject/<int:application_id>/', accept_or_reject_application, {'decision': 'reject'}, name='reject_application'),
    path('adminn/', views.adminn, name='adminn'),
    path('registration_view/', views.registration_view, name='registration_view'),
    path('dashboard/', views.marketing_manager, name='marketing_manager_dashboard'),
    path('add_property/', views.add_property, name='add_property'),
    path('update_property/<int:property_id>/', views.update_property, name='update_property'),
    path('property_detail/<int:property_id>/', views.property_detail, name='property_detail'),
    path('profile_view/', views.profile_view, name='profile_view'),

    
      path('logincustemer/', views.logincustemer, name='logincustemer'),

    path('manager/', views.manager, name='manager'),
    path('payment/', payment_view, name='payment'),
    
    path('application_for_sale/<int:property_id>/', views.application_for_sale, name='application_for_sale'),
    path('application_for_rent/<int:property_id>/', views.application_for_rent, name='application_for_rent'),
    path('addemploy/', views.addemploy, name='addemploy'),
    path('rent/', views.rent, name='rent'),
    path('buy/', views.buy, name='buy'),
    path('login/', views.login, name='login'),
    path('maintenance/', views.maintenance, name='maintenance'),
    path('manager/', views.maintenance, name='maintenance'),
    path('system_admin/', views.system_admin, name='system_admin'),
    path('add-employee/', add_employee, name='add_employee'),
    path('<int:employee_id>/active_status/', update_employee_active_status, name='update_employee_active_status'),
    path('<int:employee_id>/detail/', views.employee_detail, name='employee_detail'),
    path('system_admin_profile/', views.system_admin_profile, name='system_admin_profile'),

    path('salesperson/<int:employee_id>/', views.salesperson_profile, name='salesperson_profile'),
    path('about/', views.about, name='about'),
    path('contact_us/', contact_view, name='contact_us'),
    path('complete/<int:maintenance_id>/', views.complete_maintenance, name='complete_maintenance'),
    path('change-password/', change_password, name='change_password'),
    path('send-link/<int:maintenance_id>/', views.send_link, name='send_link'),
    path('mrk_mng/', views.mrkMng, name='mrk_mng'),
    path('forsale/', views.forsale, name='forsale'),
    path('forent/', views.forent, name='forent'),
    path('soled/', views.soled, name='soled'),
    path('rented/', views.rented, name='rented'),
    path('finance/', finance_form, name='finance_form'),
    path('financedata/', finance_with_property_data, name='finance_with_property_data'),
    path('api/finance/<int:finance_id>/', views.finance_detail_api, name='finance_detail_api'),

    path('mng/', views.mng, name='mng'),
    path('mng_rent/', views.mng_rent, name='mng_rent'),
    path('application_detail/<int:application_id>/', views.application_detail, name='application_detail'),
    path('rent_application_detail/<int:application_id>/', views.rent_application_detail, name='rent_application_detail'),
    path('update_application/<int:application_id>/', views.update_application, name='update_application'),
    path('update_application_rent/<int:application_id>/', views.update_application_rent, name='update_application_rent'),
 
    # Add other URLs as needed

]
