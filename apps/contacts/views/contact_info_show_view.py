from django.views.generic import DetailView

from apps.contacts.models import Contact


class ContactInfoShowView(DetailView):
    model = Contact
    template_name = "contacts/show_contact_info.html"
