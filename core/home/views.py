from django.shortcuts import render,redirect
from django.utils.decorators import method_decorator

from home.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import View


def home(request):
    return render(request, "index.html")


@login_required(login_url="/login_page/")
def contribution(request):
    if request.method == 'POST':
        data = request.POST
        donor_name = data.get("donor_name")
        address = data.get("address")
        phone = data.get("phone")
        email = data.get("email")
        people = data.get("people")
        # print(donor_name)
        # print(address)
        # print(people)
        Contribution.objects.create(donor_name=donor_name,  phone=phone, email=email, address=address, people=people)
        return redirect(request.path)
    return render(request, "contribution.html")


@method_decorator(login_required(login_url="/login_page/"), name='dispatch')
class ContributionListView(View):
    template_name = "available.html"

    def get(self, request, *args, **kwargs):
        queryset = Contribution.objects.all()
        if request.GET.get('search'):
            queryset = queryset.filter(address__icontains=request.GET.get('search'))
        context = {
            'contributions': queryset
        }
        return render(request, self.template_name, context)


@login_required(login_url="/login_page/")
def delete_entry(request,id):
    query = Contribution.objects.filter(id=id)
    query.delete()
    return redirect('/available/')


@login_required(login_url="/login_page/")
def update_entry(request,id):
    query = Contribution.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        query.donor_name = data.get("donor_name")
        query.address = data.get("address")
        query.phone = data.get("phone")
        query.email = data.get("email")
        query.people = data.get("people")
        query.save()
        return redirect('/available/')
    context = {
        'query': query
    }
    return render(request, "update_page.html", context)


@login_required(login_url="/login_page/")
def dashboard(request):
    total_people = 0
    queries = Contribution.objects.all()
    for query in queries:
        total_people += query.people
    context = {
        'total_people': total_people,
    }
    return render(request, "dashboard.html", context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not User.objects.filter(username=username).exists():
            messages.error(request, "User Doesn't Exist, Please Register")
            return redirect('/register_page/')
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Password Entered Incorrect")
            return redirect('/login_page')
        else:
            login(request, user)
            return redirect('/dashboard/')
    return render(request, "login_page.html")


@login_required(login_url="/login_page/")
def logout_page(request):
    logout(request)
    return redirect('/login_page')


def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        if (User.objects.filter(username=username)).exists():
            messages.info(request, "Username Already Exists")
            return redirect('/register_page/')

        user = User.objects.create(first_name=first_name,last_name=last_name,username=username)
        user.set_password(password)
        user.save()
        messages.info(request, "User Created Successfully")
        return redirect('/register_page/')
    return render(request, "register_page.html")
