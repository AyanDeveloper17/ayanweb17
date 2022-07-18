from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

class Tag(models.Model):
    name= models.CharField(max_length=100)
   

    def __str__(self):
        return self.name



class Product(models.Model):
    CATEGORY = (
        ('Indoor','Indoor'),
        ('Out door','Out door')
    )
    product_name=models.CharField(max_length=100,unique=True)
    product_price=models.FloatField()
    product_category=models.CharField(max_length=100,choices=CATEGORY)
    product_description=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return str( self.product_name)

    def get_tags(self):
        return ','.join([i.name for i in self.tag.all()])


class Order(models.Model):
    
    STATUS = (
        ('Pending','Pending'),('Out for delivery','Out for delivery'),
        ('Delivered','Delivered')
    )
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL ,null=True)
    product = models.ForeignKey(Product,on_delete=models.PROTECT,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100,choices=STATUS)
    product_quantity = models.IntegerField(null=True)
   

    def __str__(self):
        return str(self.product)
 
    def get_tags(self):
        return ','.join([i.name for i in self.product.tag.all()])

    
    