from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import DeleteView

from apps.contacts.models import Contact


class ContactDeleteView(DeleteView):
    def get(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        contact = Contact.objects.filter(pk=pk)
        contact_name = contact[0]
        total_deleted, details_of_delete = contact.delete()

        if total_deleted:
            messages.warning(request, f"Contact {contact_name} Deleted")
        else:
            messages.error(request, "Nothing deleted")
        return redirect("contacts:show_contacts")
