from django.urls import path

from . import views

app_name = "session_storage"

urlpatterns = [
    path("", views.SessionView.as_view(), name="index"),
]
