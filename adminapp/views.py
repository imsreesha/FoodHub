from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .form import AdminModelForm
from .models import *
from restaurantapp.models import Itemmodel
from userapp.models import  Usermodel
# Create your views here.
def registration(request):
    """
    Handles user registration, validating and saving form data.

    If the request method is GET, renders an empty registration form.
    If the request method is POST, validates the submitted form data.
    If the form is valid, saves the data and redirects to the home page.

    Parameters:
    - request: HttpRequest object.

    Returns:
    - HttpResponse object rendering the reg_validation.html template with the registration form.
    - Redirects to the home page on successful registration.
    """
    if request.method == 'POST':
        form_obj = AdminModelForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('/')
    else:
        form_obj =AdminModelForm()
    return render(request, 'reg_validation.html', {'form': form_obj})
def admin_home(request):
    item_count = Itemmodel.objects.all().count()
    return render(request,"admin_home.html",{'item_count':item_count})

def category(request):
    data=Maincategorymodel.objects.all()
    return render(request,"admin_category.html",{'data':data})
def allitem(request):
    item=Itemmodel.objects.all()
    return render(request,"admin_item.html",{'item':item})
def remove(request,id):
    data=Itemmodel.objects.get( Item_id=id)
    data.delete()
    return render(request, "admin_item.html")
def user(request):
    users=Usermodel.objects.all()
    return render(request,"admin_user.html",{'users':users})
