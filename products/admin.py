from django.contrib import admin

# Register your models here.
from django.contrib import admin
# Register your models here.
from .models import *

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'number', 'price', 'get_products', 'icon1', 'icon2' )
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
    list_filter = ['ordered',
                   ]
    search_fields = [

    ]

admin.site.register(Product, ProductsAdmin)
admin.site.register(OrderProduct)
admin.site.register(Order, OrderAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Category, CategoryAdmin)