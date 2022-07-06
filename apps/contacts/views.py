from django.contrib import messages
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ContactForm
from .models import Contact


def show_contacts(request: HttpRequest) -> HttpResponse:
    contacts = Contact.objects.all()
    return render(
        request,
        'contacts/show_contacts.html',
        {'contacts': contacts},
    )


def show_contact_info(request: HttpRequest, pk) -> HttpResponse:
    contact = get_object_or_404(Contact, pk=pk)
    return render(
        request,
        'contacts/show_contact_info.html',
        {'contact': contact}
    )


def create_contact(request: HttpRequest) -> HttpResponse:
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact Created')
            return redirect('contacts:show_contacts')
    else:
        form = ContactForm()

    return render(
        request,
        'contacts/create_contact.html',
        {'form': form},
    )


def update_contact(request: HttpRequest, pk) -> HttpResponse:
    contact = get_object_or_404(Contact, pk=pk)

    if request.POST:
        form = ContactForm(request.POST, instance=contact)

        if form.is_valid():
            form.save()
            messages.info(request, 'Contact Updated')
            return redirect('contacts:show_contacts')
    else:
        form = ContactForm(instance=contact)

    return render(
        request,
        'contacts/update_contact.html',
        {'form': form},
    )


def delete_contact(request: HttpRequest, pk) -> HttpResponse:
    deleted, _ = Contact.objects.filter(pk=pk).delete()

    if deleted:
        messages.warning(request, f'Contact Deleted: {deleted}')
    else:
        messages.warning(request, 'Nothing deleted')

    return redirect('contacts:show_contacts')
