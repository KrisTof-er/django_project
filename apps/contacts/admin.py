# Register your models here.
from django.contrib import admin

from .models import Contact, EmailAddress, TelegramNickname, LinkedinURL


# admin.site.register(Contact)
# admin.site.register(EmailAddress)
# admin.site.register(TelegramNickname)
# admin.site.register(LinkedinURL)
# admin.site.register(TagsChoices)


class ContactInlineAdmin(admin.TabularInline):
    model = Contact


@admin.register(EmailAddress)
class EmailAddressAdmin(admin.ModelAdmin):
    inlines = (
        ContactInlineAdmin,
    )


@admin.register(TelegramNickname)
class TelegramNicknameAdmin(admin.ModelAdmin):
    inlines = (
        ContactInlineAdmin,
    )


@admin.register(LinkedinURL)
class LinkedinURLAdmin(admin.ModelAdmin):
    inlines = (
        ContactInlineAdmin,
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    ...
