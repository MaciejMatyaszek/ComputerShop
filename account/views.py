from django.contrib import messages
from django.contrib.auth import checks
from django.contrib.auth.decorators import login_required
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
                userAdress= UserAddress.objects.create(user=user, address=address, street=street, city=city, zipcode=zipcode, phone=phone)
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

@login_required(login_url='account/login')
def updateUser(request):

    if request.method=='POST':

        password = request.POST['password']
        print(password)
        print(request.user)

        upass = User.objects.get(username=request.user)

        adress=UserAddress.objects.filter(user=request.user)
        if(upass.check_password(password)):
            upassword = User.objects.filter(username=request.user)

            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            email = request.POST['email']
            city = request.POST['city']
            street = request.POST['street']
            adress = request.POST['adress']
            zipcode= request.POST['zipcode']
            phonenumber = request.POST['phone']
            adress = UserAddress.objects.filter(user=upass).update(city=city, street=street, zipcode=zipcode, phone=phonenumber, address=adress)
            upassword.update(first_name=firstname, last_name=lastname, email=email)



        return redirect('/userprofile')

@login_required(login_url='account/login')
def updatePassword(request):

        if request.method == 'POST':

            password = request.POST['password']
            print(password)
            print(request.user)

            upass = User.objects.get(username=request.user)

            adress = UserAddress.objects.filter(user=request.user)
            if (upass.check_password(password)):
                upassword = User.objects.get(username=request.user)

                password1 = request.POST['password1']
                password2 = request.POST['password2']
                if password1 == password2:
                    upassword.set_password(password1)
                    print("Zmienilo?")
                    upassword.save()

            return redirect('/userprofile')


