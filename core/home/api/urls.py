from django.urls import path, include
from rest_framework import urls
from rest_framework import routers
from home.api.views import ContributionViewSet

router = routers.DefaultRouter()
router.register('contribution', ContributionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
