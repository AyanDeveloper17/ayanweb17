from ast import Or
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)

class OrderAdmin(admin.ModelAdmin):
    list_display =('id','customer','product','date_created','status')
admin.site.register(Order,OrderAdmin)

admin.site.register(Tag)