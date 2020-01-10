from django.contrib import admin

# Register your models here.
# Register your models here.
from django.contrib import admin
# Register your models here.
from .models import *

class UserAdressAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'zipcode', 'street', 'address' )
    prepopulated_fields = {'slug': ('user', 'city')}


admin.site.register(UserAddress)