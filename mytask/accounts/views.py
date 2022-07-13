from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.shortcuts import get_object_or_404
from .customerForm import OrderForm

# Create your views here.
def home(request):
    orders = Order.objects.all()
    cust = Customer.objects.all()
    tg = Tag.objects.all()
    total_customers = cust.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    outfor = orders.filter(status='Out for delivery').count()
    data ={
        'orders':orders,
        'cust':cust,
        'tg':tg,
        'total_orders':total_orders,
        'delivered':delivered,
        'pending':pending,
        'outfor':outfor,
    }

    
    return render(request,'dashboard.html',data)

def deletedata(request,id):
    
    get_delete = Order.objects.get(id=id)
    if request.method =='POST':
        get_delete.delete()
        return redirect('home')
    get ={'item':get_delete}

    return render(request,'delete.html',get)

def product(request):
    pro =Product.objects.all()

    return render(request,'product.html',{'pro':pro})

def customer(request,id):
    
    cust =Customer.objects.get(id=id)
    orders = cust.order_set.all()
   
    total_orders = orders.count()

    customer_details ={
        'total_orders':total_orders,
        'orders':orders,
        'cust':cust,
       
    }
    return render(request,'customer.html',customer_details)
    # except Exception as exception:
    #     print(str(exception))
    
    
def create(request,id):
    customer = Customer.objects.get(id=id)
    # form = OrderForm(instance=)
    form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        print(request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    fdata ={'form':form}
    

    return render(request,'create_orderform.html',fdata)


def updateorder(request,id):
    order = Order.objects.get(id=id)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form =OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')
    fdata ={'form':form}
    return render(request,'create_orderform.html',fdata)
