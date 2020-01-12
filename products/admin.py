from django.contrib import admin

# Register your models here.
from django.contrib import admin
# Register your models here.
from .models import *

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'number', 'price', 'get_products', 'icon1', 'icon2', 'promotion', 'new', )
    prepopulated_fields = {'slug': ('name', 'category')}
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')
    prepopulated_fields = {'slug': ('name',)}
class CategoryAdmin (admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',

                    ]
    list_display_links = [
        'user',

    ]
    list_filter = ['ordered', 'user'
                   ]
    search_fields = [

    ]
class OrderAdressAdmin(admin.ModelAdmin):
    list_display =  [ 'firstname',
                    'lastname',
                    'city',
                    'street',
                    'address',
                    'zipcode',
                    'phone',


                    ]

    list_filter = ['firstname', 'lastname', 'city']


admin.site.register(Product, ProductsAdmin)
admin.site.register(OrderProduct)
admin.site.register(Order, OrderAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(OrderAdress)
