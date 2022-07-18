from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from django.shortcuts import get_object_or_404
from .customerForm import OrderForm,CreateUserform
from .filters import Orderfilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorator import unauthenticated_user,allowed_user,admin_only
from django.contrib.auth.models import Group

from django.db.models import F

# Create your views here.

# @unauthenticated_user
def register(request):
    form = CreateUserform()
    if request.method == 'POST':
        form = CreateUserform(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            group = Group.objects.get(name='customer')
            user.groups.add(group)

            messages.success(request, 'Account Created for' +" " + username)
            return redirect('loginpage')
    pform = {'form':form}
    return render(request,'register.html',pform)


# @unauthenticated_user
# @admin_only
def loginpage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username,password = password)
        if user is not None:
          
            login(request, user)
            # return redirect('userpage')
        else:
            messages.info(request,'username or password is incorrect')
            return redirect('loginpage')

    return render(request,'loginpage.html')


def logoutuser(request):
    logout(request,)
    return redirect('loginpage')


# @login_required(login_url='loginpage')
# @admin_only
def home(request):
    orders = Order.objects.all()
    cust = Customer.objects.all()
    tg = Tag.objects.all()
    total_customers = cust.count()

    get_product_price = Order.objects.filter(id=1).annotate(total_price=F('product') * F('product_quantity'))
    for i in get_product_price:
        print(i.total_price)

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



# @login_required(login_url='loginpage')
# @allowed_user(allowed_roles=['admin'])
def product(request):
    pro =Product.objects.all()

    return render(request,'product.html',{'pro':pro})

# @login_required(login_url='loginpage')
# @allowed_user(allowed_roles=['admin'])
def customer(request,id):
    
    cust = Customer.objects.get(id=id)
    orders = cust.order_set.all().values("id","product__product_name","product__product_category","product_quantity","date_created","status").annotate(total_price = F("product_quantity") * F("product__product_price"))
   
    total_orders = orders.count()

    myfilter = Orderfilter(request.GET,queryset=orders)
    orders = myfilter.qs

    customer_details ={
        'total_orders':total_orders,
        'orders':orders,
        'cust':cust,
        'myfilter':myfilter
       
    }
    return render(request,'customer.html',customer_details)
    # except Exception as exception:
    #     print(str(exception))
    
# @login_required(login_url='loginpage')    
# @allowed_user(allowed_roles=['admin'])
def create(request,id):
    OrderFormSet = inlineformset_factory(Customer, Order,fields=('product','status','product_quantity'), extra=5)
    customer = Customer.objects.get(id=id)
    # form = OrderForm(instance=)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    # form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        print(request.POST)
        # form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('home')
    fdata ={'formset':formset}
    

    return render(request,'create_orderform.html',fdata)

# @login_required(login_url='loginpage')
# @allowed_user(allowed_roles=['admin'])
def updateorder(request,id):
    order = Order.objects.get(id=id)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form =OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')
    fdata ={'form':form}
    return render(request,'update_order.html',fdata)


# @login_required(login_url='loginpage')
# @allowed_user(allowed_roles=['admin'])
def deletedata(request,id):
    
    get_delete = Order.objects.get(id=id)
    if request.method =='POST':
        get_delete.delete()
        return redirect('home')
    get ={'item':get_delete}

    return render(request,'delete.html',get)


def userpage(request):
    return render(request,'user.html')


def calculate(request):
    pass
    # prd=Product.objects.get(id = 2).product_price
    # print(prd)
  
    # # # new =  prd.product_price()

    # # print (str(prd))
    # # print("=============================")
    # ordr=Order.objects.get(id=2).product_quantity
    


    # get_ans = (prd)
    # return get_ans
