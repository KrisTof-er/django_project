from typing import ClassVar

from django.views.generic import TemplateView

from apps.user_generator.services import generator_of_users


class UserGeneratorView(TemplateView):
    template_name = "user_generator/show_users.html"
    _DEFAULT_NUMBER_OF_USERS: ClassVar[int] = 15

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        try:
            number_of_users = data["number_of_users"]
        except KeyError:
            number_of_users = self._DEFAULT_NUMBER_OF_USERS
            data["number_of_users"] = number_of_users
        users = generator_of_users(number_of_users)
        data["users"] = users

        return data
