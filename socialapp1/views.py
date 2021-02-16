from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required


from django.contrib import messages
from .models import Profile

# Create your views here.

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        email = request.POST.get('email')
        user1 = User.objects.filter(email=email).first()
        password = request.POST.get('password')
        user = authenticate(request, username=user1, password=password)
        print(user)

        if user is not None:
            login(request, user)
            request.session['email'] = email
            return redirect('home')
        else:
            messages.info(request, "Username or Password is incorrect")
            msg = "Username or Password is incorrect"
            context = {"msg": msg}
            return render(request, 'login.html', context)
    return render(request, 'login.html')


def registerpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username=form.cleaned_data.get("username")


            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form':form,"messages":messages}
    return render(request, 'register.html',context)

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


def logoutpage(request):
    logout(request)
    return redirect('login')
