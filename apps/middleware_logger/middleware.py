import logging
from typing import Callable

from django.utils import timezone

from apps.middleware_logger.models import Log


class MiddlewareLogger:
    def __init__(self, get_response: Callable):
        """One-time configuration and initialization."""
        self.get_response = get_response
        self.logger = logging.getLogger("django")

    def __call__(self, request):
        # Code to be executed for each request before calling the middleware.
        message = f"[{request.user}] {request.path}"
        self.logger.info(f"\n![before]! - {message} ({timezone.now()})")

        # Get resp
        response = self.get_response(request)
        # Save Log object
        if "." not in request.path:
            if not Log.objects.filter(user=request.user, path=request.path).exists():
                log = Log()
                log.user = request.user
                log.path = request.path
                self.logger.info(f"___![new log creating]!___\n- user: {log.user};\n- path: {log.path}")
            else:
                log = Log.objects.get(user=request.user, path=request.path)
                log.count += 1
                self.logger.info(f"___![log updating]!___\n- count = {log.count}")
            log.last_visit = timezone.now()
            self.logger.info(f"- last visit: {log.last_visit}")
            log.save()
            self.logger.info("___![log saved]!___")

        # Code to be executed for each request/response after the middleware is called.
        self.logger.info(f"![after]! - {message} ({timezone.now()})\n")

        return response
