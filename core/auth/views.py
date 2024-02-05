from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not User.objects.filter(username=username).exists():
            messages.error(request, "User Doesn't Exist, Please Register")
            return redirect('auth/register_page/')
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Password Entered Incorrect")
            return redirect('auth/login_page')
        else:
            login(request, user)
            return redirect('/dashboard/')
    return render(request, "login_page.html")


@login_required(login_url="auth/login_page/")
def logout_page(request):
    logout(request)
    return redirect('/')


def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if (User.objects.filter(username=username)).exists():
            messages.info(request, "Username Already Exists")
            return redirect('auth/register_page/')
        if password1 != password2:
            messages.info(request, "Passwords Did not match")
            return redirect('auth/register_page/')

        user = User.objects.create(first_name=first_name, last_name=last_name, username=username, email=email)
        user.set_password(password1)
        user.save()
        messages.info(request, "User Created Successfully")
        return redirect('auth/register_page/')
    return render(request, "register_page.html")

