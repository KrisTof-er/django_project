from django.urls import path

from . import views

urlpatterns = [
    path('', views.user_generator),
    path('<int:number_of_users>', views.user_generator)
]
