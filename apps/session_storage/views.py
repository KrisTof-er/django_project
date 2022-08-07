from typing import ClassVar, Any

from django.views.generic import TemplateView


class SessionView(TemplateView):
    template_name = "session_storage/index.html"

    KEY_TO_COUNT_OF_VISITS: ClassVar[str] = "count_of_visits"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        session = self.request.session

        count_of_visits = session.get(self.KEY_TO_COUNT_OF_VISITS, 0)
        count_of_visits += 1
        session[self.KEY_TO_COUNT_OF_VISITS] = count_of_visits

        kwargs[self.KEY_TO_COUNT_OF_VISITS] = count_of_visits
        kwargs["session_id"] = session.session_key
        kwargs["session_datetime"] = session.get_expiry_date()

        return kwargs
