from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    pass
    # def wraper_func(request,*args,**kwargs):
    #     if request.user.is_authenticated:
    #         return redirect('home')
    #     else:
    #          return view_func(request,*args, **kwargs)
    # return wraper_func

def allowed_user(allowed_roles=[]):
    pass
    # def decorator(view_func):
    #     def wraper_func(request,*args,**kwargs):
    #         group = None
    #         if request.user.groups.exists():
    #             group = request.user.groups.all()[0].name
            
    #         if group in allowed_roles:
    #             return view_func(request,*args,**kwargs)
    #         else:
    #             return HttpResponse('Alert :- You are not allowed to view this page!')
    #     return wraper_func
    # return decorator

def admin_only(view_func):
    pass
    # def wraper_func(request,*args,**kwargs):
    #     group = None
    #     if request.user.groups.exists():
    #         group = request.user.groups.all()[0].name
    #         if group == "customer":
    #             return redirect('userpage')
    #         elif group == "admin":
    #             return redirect('home')


    #     else:
    #         print(group)
    #         return HttpResponse('Alert :- You are not allowed to view this page!')
    # return wraper_func