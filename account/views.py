from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.


def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method == "POST":
        username= request.POST['username']
        password= request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    else:
        return render(request,'login.html')


def register(request):

    if request.method == "POST":

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('register')
            else:
              user = User.objects.create_user(first_name=first_name,last_name=last_name,username =username,email=email,password=password )
              user.save();
              print("user created")
        else:
            print("pwd not corct")
            return redirect('register')
        return redirect('/')
    else:

     return render(request,'registration.html')