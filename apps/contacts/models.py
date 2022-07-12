from django.core.validators import URLValidator
from django.db import models
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField


# class PhoneNumber(models.Model):
#     phone = PhoneNumberField(
#         "Phone number", help_text="Phone number of contact",
#         unique=True, max_length=13
#     )
#
#     def __str__(self):
#         return f'{self.phone}'
#
#     __repr__ = __str__


class EmailAddress(models.Model):
    email = models.EmailField('Email', max_length=50)

    def __str__(self):
        return f'{self.email}'

    __repr__ = __str__


class TelegramNickname(models.Model):
    telegram = models.SlugField('Telegram', max_length=20)

    def __str__(self):
        return f'{self.telegram}'

    __repr__ = __str__


class LinkedinURL(models.Model):
    linkedin = models.CharField('Linkedin URL', max_length=50, validators=[
        URLValidator(
            message='Enter a link starting with "https://www.linkedin.com/in/"',
            schemes='https://www.linkedin.com/in/'
        )
    ])

    def __str__(self):
        return f'{self.linkedin}'

    __repr__ = __str__


class Contact(models.Model):
    contact_name = models.CharField("Contact name", help_text="Name of contact", max_length=50)
    birthday = models.DateField('Birthday', help_text='Date of birth', null=True, blank=True)

    TagsChoices = (
        ("FAMILY", 'Family'),
        ("JOB", 'Job'),
        ("FRIENDS", 'Friends'),
        ("JOURNEY", 'Journey'),
        ("EVENT", 'Event'),
        ("UNIVERSITY", 'University')
    )

    contact_tags = MultiSelectField(
        'Tags',
        help_text="Contact Tags",
        choices=TagsChoices,
        null=True,
        blank=True
    )

    phone_value = PhoneNumberField(
        "Phone number", help_text="Phone number of contact",
        max_length=13, unique=True, default='',
    )

    contact_email = models.ForeignKey(EmailAddress, on_delete=models.SET_NULL, null=True, blank=True)
    contact_telegram = models.OneToOneField(TelegramNickname, on_delete=models.SET_NULL, null=True, blank=True)
    contact_linkedin = models.OneToOneField(LinkedinURL, on_delete=models.SET_NULL, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.contact_name}'

    __repr__ = __str__
