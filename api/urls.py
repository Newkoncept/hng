from django.urls import path
from .views import meview

urlpatterns = [
    path("me/", meview)
]
