from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def index(request):
    params = {
        "logged_in": request.user.is_authenticated
    }
    return render(request, 'index.html', params)


def register(request):

    if request.method == 'POST':

        email = request.POST['email']
        username = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        if User.objects.filter(username=username).exists():
            params = {
                "success": 0,
                "message": "The email is already in use. If this email is yours, you can try to login"
            }
            return render(request, 'register.html', params)

        user = User.objects.create_user(
            username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        user.save()
        print('user created')
        return redirect('/dashboard')
    else:
        if request.user.is_authenticated:
            return redirect('/dashboard')
        return render(request, 'register.html')


def login(request):

    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if (user.is_active):
                auth.login(request, user)
                return redirect('/dashboard')
            else:
                messages.info(
                    request, 'This user is not active. Contact Admin!')
                params = {
                    "success": 0,
                    "message": "This user is not active. Contact Admin!"
                }
                return render(request, 'login.html', params)
        else:
            messages.info(request, 'Email or password is invalid')
            params = {
                "success": 0,
                "message": "Email or password is invalid"
            }
            return render(request, 'login.html', params)
    else:
        if request.user.is_authenticated:
            return redirect('/dashboard')
        return render(request, 'login.html')

def signout(request):
    logout(request)
    return redirect('/login')

@login_required(login_url='/login/')
def dashboard(request):

    if request.method == 'POST':
        return 'Method is not allowed'
    else:
        return render(request, 'dashboard.html')
