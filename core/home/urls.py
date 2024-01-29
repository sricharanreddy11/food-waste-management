from django.urls import path
from home.views import *

urlpatterns = [
    path('', login_page, name='login_page'),
    path('contribute/', ContributionCreateView.as_view(), name='contribution'),
    path('available/', ContributionListView.as_view(), name="availability"),
    path('available/<int:pk>/', ContributionDetailView.as_view()),
    path('delete_entry/<id>/', delete_entry, name='delete_entry'),
    path('update_entry/<int:pk>/', ContributionUpdateView.as_view(), name='update_entry'),
    path('dashboard/', ContributionView.as_view(), name='dashboard'),
    path('login_page/', login_page, name='login_page'),
    path('register_page/', register_page, name='register_page'),
    path('logout_page/', logout_page, name='logout_page'),
]