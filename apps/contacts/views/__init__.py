# from django.urls import reverse_lazy
# from django.views.generic import CreateView
#
# from apps.contacts.forms import ContactForm
from .contact_create_view import ContactCreateView
from .contact_delete_view import ContactDeleteView
from .contact_info_show_view import ContactInfoShowView
from .contact_update_view import ContactUpdateView
from .contacts_show_view import ContactsShowView

# class ContactCreateView(CreateView):
#     form_class = ContactForm
#     template_name = 'contacts/create_contact.html'
#     success_url = reverse_lazy('contacts:show_contacts')
