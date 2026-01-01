from django.urls import path
from . import views

urlpatterns = [
     path('',views.index,name='index'),
     path('contact/',views.contact,name='contact'),
     path('shop/',views.shop,name='shop'),
     path('register/',views.register,name='register'),
     path('login/',views.login,name='login'),
     path('logout/',views.logout,name='logout'),
     path('change_password/',views.change_password,name='change_password'),
     path('profile/',views.profile,name='profile'),
]
