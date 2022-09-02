from django.contrib import admin

from apps.middleware_logger.models import Log


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    ...
