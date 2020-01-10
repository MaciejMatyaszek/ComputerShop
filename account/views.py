from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import UserAddress

# Create your views here.

def login(request):
    url = request.POST.get('next', '/')
    print("JAka wartos: "+url)
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']

        user = auth.authenticate(username=username, password=password)


        if user is not None:
         auth.login(request,user)
         print(HttpResponseRedirect(url))
         return HttpResponseRedirect(url)


        else:
            messages.info(request, 'invalid credentials')
            return render(request, 'login.html')



    else:
        url=request.GET.get('next', '/')
        print(url)
        return render(request, 'login.html', {'next': url} )


def register(request):
    print(request.method)
    if request.method == 'POST':
        first_name= request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        street = request.POST['street']
        city = request.POST['city']
        zipcode = request.POST['zipcode']
        address = request.POST['address']
        phone = request.POST['phone']

        if username == '' or password1 == '' or last_name == '' or username == '' or password2== '' or email == '' or street == '' or city == '' or zipcode=='' or address == '' or phone == '':
            print('Bylem tutaj')
            messages.info(request, 'Uzupełnij wszystkie pola!')
            return redirect('register')
        elif password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return  redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                userAdress= UserAddress.objects.create(user=user, address=address, street=street, city=city, zipcode=zipcode)
                user.save()
                userAdress.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not maching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html' )


def logout(request):
    auth.logout(request)
    return redirect('/')