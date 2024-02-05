from django.urls import path,include

from home.api import urls as api_urls
from auth import urls as auth_urls
from home.views import *

urlpatterns = [
    path('', home, name='home'),
    path('contribute/', ContributionCreateView.as_view(), name='contribution'),
    path('available/', ContributionListView.as_view(), name="availability"),
    path('available/<int:pk>/', ContributionDetailView.as_view()),
    path('available/<int:pk>/delete/', ContributionDeleteView.as_view(), name='delete_entry'),
    path('available/<int:pk>/update/', ContributionUpdateView.as_view(), name='update_entry'),
    path('dashboard/', ContributionView.as_view(), name='dashboard'),
    path("available/<pk>/request/", request_entry, name="request_entry"),

    path("api/", include(api_urls)),
    path("auth/", include(auth_urls)),
]
