from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from apps.user_generator.services import generator_of_users


def user_generator(request: HttpRequest, number_of_users: int = 100) -> HttpResponse:
    return render(
        request,
        'user_generator/show_users.html',
        {'number_of_users': number_of_users, 'user_generator': generator_of_users(users=number_of_users)},
    )
