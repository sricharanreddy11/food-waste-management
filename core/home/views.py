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
from django.views.generic import (
    View,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView,
)


def home(request):
    contributions = Contribution.objects.all()
    total_people = sum(query.people for query in contributions)
    context = {
        'total_people': total_people
    }
    return render(request, "base.html", context)


def request_entry(request, pk):
    contribution_obj = get_object_or_404(Contribution, id=pk)
    contribution_obj.requests += 1
    contribution_obj.save()
    return redirect('availability')


class ContributionView(LoginRequiredMixin, View):
    template_name = "dashboard.html"
    login_url = "/auth/login_page/"

    def get_queryset(self):
        base_qs = Contribution.objects.all()
        if self.request.user.is_staff:
            return base_qs
        else:
            return base_qs.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        contributions = self.get_queryset()
        total_users = User.objects.count()
        total_people = sum(query.people for query in contributions)
        total_request = sum(query.requests for query in contributions)
        total_count = 0
        for _ in contributions:
            total_count += 1

        context = {
            'total_users': total_users,
            'total_people': total_people,
            'total_request': total_request,
            'total_count': total_count,
        }

        return render(request, self.template_name, context)


class ContributionCreateView(LoginRequiredMixin, CreateView):
    template_name = "contribution_form.html"
    login_url = "/auth/login_page/"
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


class ContributionListView(ListView):
    template_name = "contribution_list.html"
    login_url = '/auth/login_page/'
    model = Contribution
    context_object_name = "contributions"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            base_qs = super(ContributionListView, self).get_queryset()
            if self.request.user.is_staff:
                return base_qs
            else:
                return base_qs.filter(user=self.request.user)
        else:
            base_qs = super(ContributionListView, self).get_queryset()
            return base_qs


class ContributionDetailView(DetailView):
    template_name = "contribution_detail.html"
    model = Contribution
    context_object_name = "contribution"

    def get_queryset(self):
        base_qs = super(ContributionDetailView, self).get_queryset()
        if self.request.user.is_staff:
            return base_qs
        else:
            return base_qs.filter(user=self.request.user)

    def get_object(self, queryset=None):
        return get_object_or_404(Contribution, pk=self.kwargs['pk'])


class ContributionUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "contribution_form.html"
    model = Contribution
    context_object_name = "query"
    fields = ["donor_name", "address", "phone", "email", "people"]
    success_url = reverse_lazy('availability')

    def get_queryset(self):
        base_qs = super(ContributionUpdateView, self).get_queryset()
        if self.request.user.is_staff:
            return base_qs
        else:
            return base_qs.filter(user=self.request.user)

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Contribution updated Successfully")
        return super(ContributionUpdateView, self).form_valid(form)


class ContributionDeleteView(LoginRequiredMixin, DeleteView):
    model = Contribution
    context_object_name = "contribution"
    template_name = "contribution_confirm_delete.html"
    login_url = "/auth/login_page/"
    success_url = reverse_lazy('availability')

    def get_queryset(self):
        base_qs = super(ContributionDeleteView, self).get_queryset()
        if self.request.user.is_staff:
            return base_qs
        else:
            return base_qs.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Contribution deleted successfully")
        return super().delete(request, *args, **kwargs)


"""
    Function Based Views for Authentication
"""


# class MyLoginView(LoginView):
#     redirect_authenticated_user = True
#     template_name = "login_page.html"
#     fields = ["username", "password"]
#
#     def get_success_url(self):
#         return reverse_lazy('dashboard')
#
#     def form_invalid(self, form):
#         messages.error(self.request, 'Invalid Username or password')
#         return self.render_to_response(self.get_context_data(form=form))
#
#
# class RegisterView(CreateView):
#     template_name = 'register_page.html'
#     form_class = RegistrationForm
#     model = User
#     success_url = reverse_lazy('register_page')  # Change this to your desired success URL
#
#     def form_valid(self, form):
#         response = super().form_valid(form)
#         messages.success(self.request, "User Created Successfully")
#         return response

