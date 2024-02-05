from django.urls import path,include

from home.api import urls
from home.views import *

urlpatterns = [
    path('', home, name='home'),
    path('contribute/', ContributionCreateView.as_view(), name='contribution'),
    path('available/', ContributionListView.as_view(), name="availability"),
    path('available/<int:pk>/', ContributionDetailView.as_view()),
    path('available/<int:pk>/delete/', ContributionDeleteView.as_view(), name='delete_entry'),
    path('available/<int:pk>/update/', ContributionUpdateView.as_view(), name='update_entry'),
    path('dashboard/', ContributionView.as_view(), name='dashboard'),
    path('login_page/', login_page, name='login_page'),
    path('register_page/', register_page, name='register_page'),
    path('logout_page/', logout_page, name='logout_page'),
    path("available/<pk>/request/", request_entry, name="request_entry"),

    path("api/", include(urls)),
]
