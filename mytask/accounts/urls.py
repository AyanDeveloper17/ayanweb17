from django.urls import path
from accounts import views

urlpatterns = [
    path('',views.home,name='home'),
    path('product/',views.product,name='product'),
    path('customer/<int:id>/',views.customer,name='customer'),
    path('deletedata/<int:id>',views.deletedata,name='deletedata'),
    path('create/<int:id>/',views.create,name='create'),
    path('updateorder/<int:id>/',views.updateorder,name='updateorder')
    
]
