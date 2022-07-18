from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('product/',product,name='product'),
    path('customer/<int:id>/',customer,name='customer'),
    path('deletedata/<int:id>',deletedata,name='deletedata'),
    path('create/<int:id>/',create,name='create'),
    path('updateorder/<int:id>/',updateorder,name='updateorder'),
    path('register/',register,name='register'),
    path('loginpage/',loginpage,name='loginpage'),
    path('logoutuser/',logoutuser,name='logoutuser'),
    path('userpage/',userpage,name='userpage'),
    path('calculate/',calculate,name='calculate'),

]
