from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegistrationForm


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not User.objects.filter(username=username).exists():
            messages.error(request, "User Doesn't Exist, Please Register")
            return redirect('/auth/register_page/')
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Password Entered Incorrect")
            return redirect('/auth/login_page')
        else:
            login(request, user)
            return redirect('/dashboard/')
    return render(request, "auth/login_page.html")


@login_required(login_url="/auth/login_page/")
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
            return redirect('/auth/register_page/')
        if password1 != password2:
            messages.info(request, "Passwords Did not match")
            return redirect('/auth/register_page/')

        user = User.objects.create(first_name=first_name, last_name=last_name, username=username, email=email)
        user.set_password(password1)
        user.save()
        messages.info(request, "User Created Successfully")
        return redirect('/auth/register_page/')
    return render(request, "auth/register_page.html")

# if request.method == "POST":
#     form = RegistrationForm(request.POST)
#     if form.is_valid():
#         user = form.save()
#         messages.info(request, "User Created Successfully")
#         return redirect('auth/register_page/')
# else:
#     form = RegistrationForm()
# return render(request, "register_page.html", {'form': form})


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

