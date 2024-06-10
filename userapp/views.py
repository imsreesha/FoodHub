from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from userapp.models import *
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse


# Create your views here.
def home(request):
    restaurants = Restaurantmodel.objects.all()
    return render(request, "Home.html", {'restaurants': restaurants})



def contact(request):
    return render(request,"contact.html")
def help(request):
    return render(request,"help.html")

def items_by_category(request, category):
    items = Itemmodel.objects.filter(Category__Maincategory=category)
    return render(request, 'item.html', {'items': items, 'category': category})


def login(request):
    if request.method == 'POST':
        contact = request.POST.get('contact')
        password = request.POST.get('password')

        user = Usermodel.objects.filter(User_phone=contact,User_password=password).first()


        if user is not None:
            request.session['user_id']=user.User_id
            request.session['user_name'] = user.User_name

            return redirect('home')
        else:

            return render(request, 'login.html', {'error': 'Invalid phone number or password'})
    else:
        return render(request, 'login.html')


def start(request):
    return render(request,"start.html")


def register(request):

    if request.method == 'POST':
        print("password doesnt match")
        name = request.POST.get('name')
        phone = request.POST.get('contact')
        passwordd= request.POST.get('password')
        passwordn= request.POST.get('password2')
        if passwordd != passwordn:
            error='Passwords do not match'
            return render(request, "user_regster.html",{'error':error})
        else:
            user_obj = Usermodel()
            print("object created")
            user_obj.User_name = name
            user_obj.User_phone = phone
            user_obj.User_password = passwordd
            user_obj.save()
            return redirect('/login')
    return render(request,"user_regster.html")





def search(request):
    if request.method == "POST":
        search_item = request.POST.get('search')

        if search_item:
            items = Itemmodel.objects.filter(
                Q(Item_name__icontains=search_item) |
                Q(Category__Maincategory__icontains=search_item)|Q(host_id__Address__icontains=search_item)
            )
        else:
            items = Itemmodel.objects.all()

        return render(request, "search.html", {'item': items})
    else:
        items = Itemmodel.objects.all()
        return render(request, "search.html", {'item': items})


def cart(request):
    return render(request,"cartnew.html")
def restaurant(request,id):
    rest_data=Restaurantmodel.objects.filter(Restaurant_id=id)
    item_data=Itemmodel.objects.filter(host_id=id)
    menu_data=''
    if request.method=='POST':
        menu_data=request.POST.get('menusrch')
        if menu_data:
            item_data=item_data.filter(Item_name__icontains=menu_data)
    return render(request,'restaurant.html',{'rest_data':rest_data,'items':item_data,'menu_srch':menu_data})


def load_content(request, button_text):
    user_id = request.session.get('user_id')

    if user_id:
        user_details = Usermodel.objects.get(User_id=user_id)
        address_details = Addressmodel.objects.filter(User_id=user_id)



        context = {
            'button_text': button_text,
            'user_details': user_details,
            'address_details': address_details,
        }
        return render(request, 'profile.html', context)
    else:
        messages.warning(request, 'You need to log in to access your profile.')
        return HttpResponseRedirect(reverse('login'))





def change_password(request):
    user_id = request.session.get('user_id')

    if user_id:
        if request.method == 'POST':
            current_password = request.POST.get('current_password')
            new_password = request.POST.get('new_password')
            confirm_new_password = request.POST.get('confirm_new_password')

            user = Usermodel.objects.get(User_id=user_id)
            if user.User_password == current_password:
                if new_password == confirm_new_password:
                    user.User_password = new_password
                    user.save()
                    request.session.flush()
                    return redirect('home')
                else:
                    return render(request, 'profile.html', {'error': "New passwords don't match."})
            else:
                return render(request, 'profile.html', {'error': 'Invalid current password.'})
        else:
            return render(request, 'profile.html')
    else:
        return redirect('login')

def add_address(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        if user_id:
            name = request.POST.get('Name')
            mobile_number = request.POST.get('Mobile number')
            address = request.POST.get('Address')
            city = request.POST.get('city')
            state = request.POST.get('state')
            pincode = request.POST.get('pincode')

            if city and state:
                new_address = Addressmodel.objects.create(User_id_id=user_id, Street=address,
                                                          Location=address, Pincode=pincode)
                new_address.save()
                if new_address:
                    messages.success(request, 'Address added successfully.')
                    return redirect('home')
            else:
                messages.error(request, 'City and state are required fields.')
                return redirect('home')
    messages.error(request, 'Failed to add address. Please try again.')
    return redirect('home')

def delete_address(request):
    if request.method == 'POST':
        address_id = request.POST.get('address_id')
        try:
            address = Addressmodel.objects.get(pk=address_id)
            address.delete()
            messages.success(request, 'Address deleted successfully.')
        except Addressmodel.DoesNotExist:
            messages.error(request, 'Address does not exist.')
    return redirect('home')


def logout(request):

    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('home')

from django.shortcuts import redirect
from django.urls import reverse
from .models import Itemmodel, Wishlistmodel

def addwishlist(request, id):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        try:
            item = Itemmodel.objects.get(Item_id=id)
            restaurant_id = item.host_id.Restaurant_id
            if not Wishlistmodel.objects.filter(Item=id, User=user_id).exists():
                wishlist_obj = Wishlistmodel(Item=item, User_id=user_id)
                wishlist_obj.save()
                item.is_in_wishlist = True
                item.save()
                return redirect(reverse('restaurant_detail', args=[restaurant_id]))
            else:
                return redirect(reverse('restaurant_detail', args=[restaurant_id]))
        except Itemmodel.DoesNotExist:
            print("Item does not exist")
            return redirect(reverse('restaurant_detail', args=[restaurant_id]))
        except Exception as e:
            print("Error:", e)
            return redirect(reverse('restaurant_detail', args=[restaurant_id]))
    else:
        return redirect('/login')


import logging
from django.shortcuts import render, redirect
from .models import Wishlistmodel

logger = logging.getLogger(__name__)

from django.shortcuts import render, redirect
from .models import Wishlistmodel

def wishlist(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        print("User ID from session:", user_id)
        wishlist_data = Wishlistmodel.objects.filter(User=user_id)
        wishlist_count = wishlist_data.count()
        return render(request, 'wishlist.html', {'wishlist_data': wishlist_data, 'wishlist_count': wishlist_count})
    else:
        print("User not logged in")

        return redirect('/login')



def delwishlistitem(request,id):
    wishlist_data= Wishlistmodel.objects.get(Item=id)
    wishlist_data.delete()
    item_data=Itemmodel.objects.get(Item_id=id)
    item_data.is_in_wishlist=False
    item_data.save()
    return redirect('/wishlist')

def addtocart(request,id):
    if 'user' in request.session:
        user=request.session['user_id']
        cart_data=Cartmodel.objects.filter(item_id=id)
        cart_count=cart_data.count()
        return render(request,"cartnew.html",{'cart_data':cart_data,'cart_count':cart_count})

def removecart(request,id):
    cart_data= Wishlistmodel.objects.get(Item=id)
    cart_data.delete()
    return redirect('/cart')




