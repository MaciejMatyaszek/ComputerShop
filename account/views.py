from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.

def login(request):



    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']

        user = auth.authenticate(username=username, password=password)
        print(request.get_full_path())
        print(request.GET.get('url'))
        print(request.GET.get('url') is not None)

        if user is not None:
         auth.login(request,user)
         return redirect("/")


        else:
            messages.info(request, 'invalid credentials')
            return render(request, 'login.html')



    else:

        return render(request, 'login.html')


def register(request):
    print(request.method)
    if request.method == 'POST':
        first_name= request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if username == '' or password1 == '' or last_name == '' or username == '' or password2== '' or email == '':
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
                user.save()
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