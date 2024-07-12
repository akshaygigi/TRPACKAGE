from django.urls import path
from .import views

urlpatterns = [
    path('', views.IndexView,name='home'),
    path('signup/', views.signup,name='signup'),
    path('loginss/', views.loginss,name='loginss'),
    path('packages/',views.package_list,name='packages'),
    path('payments/',views.payments,name='payments')

    ]