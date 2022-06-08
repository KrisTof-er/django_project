from django.http import HttpResponse

from user_generator.services import generator_of_users


def user_generator(request, number_of_users: int = 100) -> HttpResponse:
    list_of_users = list(generator_of_users(number_of_users))
    return HttpResponse(f"""<h2><u>{number_of_users} Users:</u></h2>
<p>{'<br>'.join(list_of_users)}</p>""")
