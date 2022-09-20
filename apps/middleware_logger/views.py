from django.views.generic import ListView

from apps.middleware_logger.models import Log


class LoggerCounterView(ListView):
    model = Log
    template_name = "logger_counter/show_logs.html"
    context_object_name = "logs"
