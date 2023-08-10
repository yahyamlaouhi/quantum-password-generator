from django.urls import path

from . import views

urlpatterns = [
    path("", views.generate_random_password, name="generate_random_password"),
]