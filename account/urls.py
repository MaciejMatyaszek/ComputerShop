from django.urls import path
from . import views
from .views import (
    updateUser,
    updatePassword,
)

urlpatterns = [
    path('register',  views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('updateuser', updateUser, name='upadteuser'),
    path('updatepassword', updatePassword, name='updatepassword'),



]