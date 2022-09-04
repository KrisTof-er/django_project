from datetime import datetime

from django.db import models


class Log(models.Model):
    user = models.CharField("User", max_length=200)
    path = models.CharField("Request Path", max_length=200)
    count = models.PositiveIntegerField("Number of requests", default=1)
    last_visit = models.DateTimeField("Last Visit", null=True, blank=True, default=datetime.now)

    def __str__(self):
        return f"{self.user} ({self.path})"

    __repr__ = __str__
