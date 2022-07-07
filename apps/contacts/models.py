from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    contact_name = models.CharField("Contact name", help_text="Name of contact", max_length=50)
    phone_value = PhoneNumberField(
        "Phone number", help_text="Phone number of contact",
        unique=True, max_length=13, null=False, blank=False
    )

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.contact_name} ({self.phone_value})'

    __repr__ = __str__
