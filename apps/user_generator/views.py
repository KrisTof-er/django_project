from django.http import HttpResponse

from apps.user_generator.services import generator_of_users


def user_generator(request, number_of_users: int = 100) -> HttpResponse:
    return HttpResponse(f"""<h2><u>{number_of_users} Users:</u></h2>
<ol>
{''.join(f"<li>{user.name} <em>{user.email}</em></li>" for user in generator_of_users(users=number_of_users))}
</ol>""")
