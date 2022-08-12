from django.urls import path

from . import views

app_name = "caesar"

urlpatterns = [
    path("", views.encrypt_or_decrypt, name="index"),
]
