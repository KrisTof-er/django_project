from django.contrib import messages
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ContactForm  # , EmailForm, TelegramForm, LinkedinForm
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
        contact_form = ContactForm(request.POST)
        # email_form = EmailForm(request.POST)
        # telegram_form = TelegramForm(request.POST)
        # linkedin_form = LinkedinForm(request.POST)
        if contact_form.is_valid():
            # contact_data = Contact(
            #     contact_name=contact_form.cleaned_data["contact_name"],
            #     birthday=contact_form.cleaned_data["birthday"],
            #     contact_tags=contact_form.cleaned_data["contact_tags"],
            #     phone_value=contact_form.cleaned_data["phone_value"],
            #     # contact_email=email_form.fields["email"],
            #     # contact_telegram=telegram_form,
            #     # contact_linkedin=linkedin_form,
            # )
            # contact_data.save()
            contact_form.save()
            # email_form.save()
            # telegram_form.save()
            # linkedin_form.save()
            messages.success(request, 'Contact Created')
            return redirect('contacts:show_contacts')
    else:
        contact_form = ContactForm()
        # email_form = EmailForm()
        # telegram_form = TelegramForm()
        # linkedin_form = LinkedinForm()

    return render(
        request,
        'contacts/create_contact.html',
        {'contact_form': contact_form,
         # 'email_form': email_form, 'telegram_form': telegram_form, 'linkedin_form': linkedin_form
         },
    )


def update_contact(request: HttpRequest, pk) -> HttpResponse:
    contact = get_object_or_404(Contact, pk=pk)

    if request.POST:
        contact_form = ContactForm(request.POST, instance=contact)
        # email_form = EmailForm(request.POST)
        # telegram_form = TelegramForm(request.POST)
        # linkedin_form = LinkedinForm(request.POST)
        if contact_form.is_valid():
            # contact_data = Contact(
            #     contact_name=contact_form.cleaned_data["contact_name"],
            #     birthday=contact_form.cleaned_data["birthday"],
            #     contact_tags=contact_form.cleaned_data["contact_tags"],
            #     phone_value=contact_form.cleaned_data["phone_value"],
            #     # contact_email=email_form["email"],
            #     # contact_telegram=telegram_form["telegram"],
            #     # contact_linkedin=linkedin_form["linkedin"],
            # )
            # contact_data.save()
            contact_form.save()
            # email_form.save()
            # telegram_form.save()
            # linkedin_form.save()
            messages.success(request, 'Contact Updated')
            return redirect('contacts:show_contacts')
    else:
        contact_form = ContactForm(instance=contact)
        # email_form = EmailForm()
        # telegram_form = TelegramForm()
        # linkedin_form = LinkedinForm()

    return render(
        request,
        'contacts/update_contact.html',
        {'contact_form': contact_form,
         # 'email_form': email_form, 'telegram_form': telegram_form, 'linkedin_form': linkedin_form
         },
    )


def delete_contact(request: HttpRequest, pk) -> HttpResponse:
    deleted, _ = Contact.objects.filter(pk=pk).delete()

    if deleted:
        messages.warning(request, f'Contact Deleted: {deleted}')
    else:
        messages.warning(request, 'Nothing deleted')

    return redirect('contacts:show_contacts')
