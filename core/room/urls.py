from django.urls import path
from . import views


urlpatterns = [
    path("<int:room_name>/", views.room, name="room"),
]