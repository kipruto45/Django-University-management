from .models import *
from django.shortcuts import render

def professor_required(function):
    def wrapper(request,*args,**kwargs):
        if (request.user.role.role != 'Profesor'):
            return render(request,'error.html')
        else:
            return function(request,*args,**kwargs)
    return wrapper


def admin_required(function):
    def wrapper(request,*args,**kwargs):
        if (request.user.role.role != 'Admin'):
            return render(request,'error.html')
        else:
            return function(request,*args,**kwargs)
    return wrapper


def student_required(function):
    def wrapper(request,*args,**kwargs):
        if (request.user.role.role != 'Student'):
            return render(request,'error.html')
        else:
            return function(request,*args,**kwargs)
    return wrapper