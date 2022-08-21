from django import forms

from apps.contacts.models import Contact


class ContactForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper(self)
    #     self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Contact
        fields = ("contact_name", "avatar", "birthday", "contact_tags")
