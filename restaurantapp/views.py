from django.shortcuts import render,redirect,HttpResponseRedirect
from restaurantapp.models import *
from adminapp.models import *
from userapp.models import *
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, get_object_or_404


# Create your views here.
def host_login(request):
        if request.method == 'POST':
            contact = request.POST.get('contact')
            password = request.POST.get('password')

            host =Restaurantmodel.objects.filter(Phone_no=contact,Password=password).first()

            if host is not None:
                    request.session['host_id'] = host.Restaurant_id
                    request.session['host_name'] = host.Restaurant_name
                    return redirect('host_home')
            else:

                return render(request, 'host_login.html')
        else:
            return render(request, 'host_login.html')
def load_content(request, button_text):
    user_id = request.session.get('host_id')
    coupons=Couponmodel.objects.all()

    if user_id:
        try:
            host_details = Restaurantmodel.objects.get(Restaurant_id=user_id)
            context = {
                'button_text': button_text,
                'host_details': host_details,
                'coupons':coupons,
            }
            return render(request, 'host_profile.html', context)
        except Restaurantmodel.DoesNotExist:
            messages.error(request, 'Restaurant not found.')
    else:
        messages.warning(request, 'You need to log in to access your profile.')

    return HttpResponseRedirect(reverse('host_login'))
def host_password(request):
    host_id = request.session.get('host_id')

    if host_id:
        if request.method == 'POST':
            current_password = request.POST.get('current_password')
            new_password = request.POST.get('new_password')
            confirm_new_password = request.POST.get('confirm_new_password')

            user = Restaurantmodel.objects.get(Restaurant_id=host_id)
            if user.Password== current_password:
                if new_password == confirm_new_password:

                    user.Password = new_password
                    user.save()
                    request.session.flush()
                    return redirect('host_login')
                else:
                    return render(request, 'host_home.html', {'error': "New passwords don't match."})
            else:
                return render(request, 'host_home.html', {'error': 'Invalid current password.'})
        else:
            return render(request, 'host_home.html')
    else:
        return redirect('host_login')
def add_item(request):
    if request.method == 'POST':
        host_id = request.session.get('host_id')

        if host_id:
            try:
                host = Restaurantmodel.objects.get(Restaurant_id=host_id)

                item_name = request.POST.get('item_name')
                description = request.POST.get('description')
                price = request.POST.get('price')
                image = request.FILES.get('image')
                quantity = request.POST.get('quantity')
                start_time = request.POST.get('start_time')
                end_time = request.POST.get('end_time')
                category_id = request.POST.get('category')
                category = Maincategorymodel.objects.get(Maincategory_id=category_id)

                new_item = Itemmodel(
                    Item_name=item_name,
                    Description=description,
                    Price=price,
                    Image=image,
                    Quantity=quantity,
                    Start_time=start_time,
                    End_time=end_time,
                    Category=category,
                    host_id=host,
                    status='active'
                )

                new_item.save()
                messages.success(request, 'Item added successfully.')

                return redirect(reverse('host_home'))

            except Restaurantmodel.DoesNotExist:
                messages.error(request, 'Host not found.')

        else:
            messages.warning(request, 'You need to log in to add items.')
        return redirect('host_login')

    else:
        categories = Maincategorymodel.objects.all()
        print("Categories:", categories)
        return render(request, 'add_item.html', {'categories': categories})
def delete_item(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(Itemmodel, Item_id=item_id)
        item.delete()
        return redirect('host_home')
    return redirect('host_home')

def host_home(request):
    user_id = request.session.get('host_id')
    if user_id:
        items = Itemmodel.objects.filter(host_id=user_id)
        restaurant_name = "Restaurant Name"

        context = {
            'items': items,
            'Restaurant_name': restaurant_name
        }
        return render(request, 'host_home.html', context)
    else:
        return render(request, 'host_login.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Couponmodel

def add_coupon(request):
    if request.method == 'POST':
        coupon_code = request.POST.get('Coupon-code')
        is_expired = request.POST.get('is-expired', False)
        discount_price = request.POST.get('discount-price')
        minimum_amnt = request.POST.get('minimum_amnt')

        new_coupon = Couponmodel(
            Coupon_code=coupon_code,
            is_expired=is_expired,
            discount_price=discount_price,
            minimum_amnt=minimum_amnt
        )

        new_coupon.save()

        messages.success(request, 'Coupon added successfully.')
        return redirect('host_home')

    return render(request, 'restaurant.html')

from django.contrib import messages
from .models import Eventmodel, Couponmodel, Restaurantmodel
from django.shortcuts import redirect

def add_event(request):
    coupons = Couponmodel.objects.all()

    if request.method == 'POST':
        host_id = request.session.get('host_id')
        if host_id:
            event_name = request.POST.get('event_name')
            description = request.POST.get('description')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            status = request.POST.get('status')
            coupon_id = request.POST.get('coupon')

            try:
                host_restaurant = Restaurantmodel.objects.get(Restaurant_id=host_id)

                new_event = Eventmodel(
                    event_name=event_name,
                    description=description,
                    start_date=start_date,
                    end_date=end_date,
                    status=status,
                    coupon_id=coupon_id
                )

                new_event.save()
                return redirect('host_home')

            except Restaurantmodel.DoesNotExist:
                messages.error(request, 'Host restaurant not found.')

    messages.error(request, 'Failed to add event. Please try again.')
    return redirect('host_home')