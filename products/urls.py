from django.urls import path
from . import views
from products.views import ProductList
from .views import (
    HomeView,
    ItemDetailView,
    add_to_cart,
    updateQuantity,
    purchase,
    categoryLaptops,
    search,
    shop,
    delete,
    deleteAdd,
    userProfile,

)

app_name = 'ComputerShop'

urlpatterns = [
    path('', HomeView.as_view(), name='news_list'),
    path('', search, name='szukaj'),
    path('product/<slug>', ItemDetailView.as_view(), name='productdetail'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-to-cart/<slug>/updateQuantity', updateQuantity, name='updateQuantity'),
    path('cart', views.OrderView, name='orderView'),
    path('cartupdateQuantity', views.OrderView, name='cartupdateQuantity'),
    path('buy', views.buy, name='buy'),
    path('purchase', purchase, name='purchase'),
    path('c/<slug>', categoryLaptops, name='laptops' ),
    path('c', shop, name='shop'),
    path('shop', search, name='search'),
    path('delete', delete, name='delete' ),
    path('add-to-cart/<slug>/delete', deleteAdd, name='del'),
    path('userprofile', userProfile, name='userprofile'),


]