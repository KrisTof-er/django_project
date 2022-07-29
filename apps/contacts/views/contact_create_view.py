from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.contacts.forms import ContactForm


class ContactCreateView(CreateView):
    form_class = ContactForm
    template_name = 'contacts/create_contact.html'
    success_url = reverse_lazy('contacts:show_contacts')
