from django.views.generic import ListView

from apps.contacts.models import Contact


class ContactsShowView(ListView):
    model = Contact
    template_name = "contacts/show_contacts.html"
    context_object_name = "contacts"
