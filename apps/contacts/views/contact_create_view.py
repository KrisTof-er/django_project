from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.contacts.models import Contact


class ContactCreateView(CreateView):
    model = Contact
    fields = ["contact_name", "avatar", "birthday", "contact_tags"]
    template_name = "contacts/create_contact.html"
    success_url = reverse_lazy("contacts:show_contacts")
