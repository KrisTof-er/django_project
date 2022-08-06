from django.contrib import admin

from .models import Contact, ContactTag, ContactData


class ContactDataInlineAdmin(admin.TabularInline):
    model = ContactData


class ContactInlineAdmin(admin.TabularInline):
    model = Contact.contact_tags.through


@admin.register(ContactTag)
class ContactTagAdmin(admin.ModelAdmin):
    inlines = (ContactInlineAdmin,)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = (ContactDataInlineAdmin,)


@admin.register(ContactData)
class ContactDataAdmin(admin.ModelAdmin):
    ...
