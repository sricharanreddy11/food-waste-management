from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from home.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import View,ListView, DetailView, CreateView, UpdateView, DeleteView


def home(request):
    return render(request, "index.html")


class ContributionView(LoginRequiredMixin, View):
    template_name = "dashboard.html"
    login_url = "/login_page/"

    def get(self, request, *args, **kwargs):
        contributions = Contribution.objects.all()
        total_people = sum(query.people for query in contributions)

        context = {
            'total_people': total_people,
        }

        return render(request, self.template_name, context)


class ContributionCreateView(LoginRequiredMixin, CreateView):
    template_name = "contribution_form.html"
    model = Contribution
    context_object_name = "form"
    fields = ["donor_name", "address", "phone", "email", "people"]
    success_url = reverse_lazy('contribution')

    def get_queryset(self):
        base_qs = super(ContributionCreateView, self).get_queryset()
        return base_qs.filter(user=self.request.user)

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Contribution Created Successfully")
        return super(ContributionCreateView, self).form_valid(form)


class ContributionUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "contribution_form.html"
    model = Contribution
    context_object_name = "query"
    fields = ["donor_name", "address", "phone", "email", "people"]
    success_url = reverse_lazy('contribution')

    def get_queryset(self):
        base_qs = super(ContributionUpdateView, self).get_queryset()
        return base_qs.filter(user=self.request.user)

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Contribution updated Successfully")
        return super(ContributionUpdateView, self).form_valid(form)


class ContributionListView(LoginRequiredMixin, ListView):
    template_name = "contribution_list.html"
    login_url = '/login_page/'
    model = Contribution
    context_object_name = "contributions"

    def get_queryset(self):
        base_qs = super(ContributionListView, self).get_queryset()
        return base_qs.filter(user=self.request.user)


class ContributionDetailView(LoginRequiredMixin, DetailView):
    template_name = "contribution_detail.html"
    model = Contribution
    context_object_name = "contribution"

    def get_queryset(self):
        base_qs = super(ContributionDetailView, self).get_queryset()
        return base_qs.filter(user=self.request.user)

    def get_object(self, queryset=None):
        return get_object_or_404(Contribution, pk=self.kwargs['pk'])


# class ContributionDeleteView(LoginRequiredMixin, DeleteView):


@login_required(login_url="/login_page/")
def delete_entry(request,id):
    query = Contribution.objects.filter(id=id)
    query.delete()
    return redirect('/available/')


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
