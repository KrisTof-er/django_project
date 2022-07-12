from django import forms

from apps.contacts.models import Contact  # , EmailAddress, TelegramNickname, LinkedinURL


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'contact_name', 'birthday', 'contact_tags', 'phone_value',
            # 'contact_email', 'contact_telegram', 'contact_linkedin'
        )

# class EmailForm(forms.ModelForm):
#     class Meta:
#         model = EmailAddress
#         fields = ('email',)


# class TelegramForm(forms.ModelForm):
#     class Meta:
#         model = TelegramNickname
#         fields = ('telegram',)


# class LinkedinForm(forms.ModelForm):
#     class Meta:
#         model = LinkedinURL
#         fields = ('linkedin',)
