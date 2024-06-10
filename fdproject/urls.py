"""
URL configuration for fdproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from userapp import views as userview
from restaurantapp import views as restview
from adminapp import views as adminview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',userview.start,name='start'),
    path('home',userview.home,name='home'),
    path('category/<str:category>/',userview.items_by_category, name='category_page'),
    path('contact',userview.contact,name='contact'),
    path('help',userview.help,name='help'),
    path('login',userview.login,name='login'),
    path('register',userview.register,name='register'),
    path('restaurant/<int:id>/',userview.restaurant, name='restaurant_detail'),
    path('search',userview.search,name='search'),
    path('restaurant/addtoWishlist/<int:id>/', userview.addwishlist, name='add_to_wishlist'),
    path('wishlist',userview.wishlist,name='wishlist'),
    path('delwishlistitem/<int:id>',userview.delwishlistitem),
    path('load_content/<str:button_text>/',userview.load_content, name='load_content'),
    path('change_password/',userview.change_password, name='change_password'),
    path('add_address/',userview .add_address, name='add_address'),
    path('delete_address/',userview.delete_address, name='delete_address'),
    path('logout/',userview.logout, name='logout'),
    path('login/',userview.login,name='login'),
    path('addtocart<int:id>',userview.addtocart,name='addtocart'),
    path('removecart<int:id>',userview.removecart,name='removecart'),
    path('host_login',restview.host_login,name='host_login'),
    path('hostpage/<str:button_text>/', restview.load_content, name='hostpage'),
    path('host_password/', restview.host_password, name='host_password'),
    path('add_item/', restview.add_item, name='add_item'),
    path('host_home', restview.host_home,name='host_home'),
    path('delete_item/<int:item_id>/',restview.delete_item, name='delete_item'),
    path('add_event/', restview.add_event, name='add_event'),
    path('add_coupon/', restview.add_coupon, name='add_coupon'),
    path('admin_home',adminview.admin_home),
    path('category',adminview.category,name='category'),
    path('item', adminview.allitem, name='item'),
    path('remove/<int:id>/',adminview.remove),
    path('adduser', adminview.user, name='adduser'),

]
if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
