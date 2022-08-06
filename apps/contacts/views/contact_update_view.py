from django.urls import reverse_lazy
from django.views.generic import UpdateView

from apps.contacts.models import Contact


class ContactUpdateView(UpdateView):
    model = Contact
    fields = ["contact_name", "birthday", "contact_tags"]
    template_name = "contacts/update_contact.html"
    success_url = reverse_lazy("contacts:show_contacts")
