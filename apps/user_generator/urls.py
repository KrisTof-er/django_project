from django.urls import path

from . import views

app_name = "user_generator"

urlpatterns = [
    path("", views.UserGeneratorView.as_view(), name="index"),
    path("<int:number_of_users>", views.UserGeneratorView.as_view()),
    path("<int:number_of_users>/", views.UserGeneratorView.as_view()),
]
