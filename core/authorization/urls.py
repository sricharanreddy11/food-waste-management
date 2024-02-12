from django.urls import path,include
from .views import *


urlpatterns = [
    path('login_page/', login_page, name='login_page'),
    path('register_page/', register_page, name='register_page'),
    path('logout_page/', logout_page, name='logout_page'),
]