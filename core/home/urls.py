from django.urls import path
from home.views import *

urlpatterns = [
    path('', login_page, name='login_page'),
    path('contribute/', contribution, name='contribution'),
    path('available/', ContributionListView.as_view(), name="availability"),
    path('delete_entry/<id>/', delete_entry, name='delete_entry'),
    path('update_entry/<id>/', update_entry, name='update_entry'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login_page/', login_page, name='login_page'),
    path('register_page/', register_page, name='register_page'),
    path('logout_page/', logout_page, name='logout_page'),
]