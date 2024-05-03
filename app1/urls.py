from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('all_helper',views.all_helper,name='all_helper'),
    path('add_helper',views.add_helper,name='add_helper'),
    path('all_customer',views.all_customers,name='all_customer'),
    path('add_customer',views.add_customer,name='add_customer'),
    path('assign_helper',views.assign_helper,name='assign_helper'),
    path('free_helper',views.free_helper,name='free_helper')
]