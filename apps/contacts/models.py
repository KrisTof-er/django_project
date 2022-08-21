import re
import uuid

from django import forms
from django.conf import settings
from django.db import models


class ContactData(models.Model):
    contact = models.ForeignKey(
        "Contact",
        on_delete=models.CASCADE,
        default=None,
    )

    ContactChoices = (
        ("PHONE_NUMBER", "Phone Number"),
        ("EMAIL_ADDRESS", "Email Address"),
        ("TELEGRAM_NICKNAME", "Telegram Nickname"),
        ("LINKEDIN_ID", "LinkedIn ID"),
    )

    contact_type = models.CharField(
        "Contact type",
        max_length=30,
        choices=ContactChoices,
        default="PHONE_NUMBER",
    )
    value = models.CharField(
        "Value",
        max_length=100,
        default="",
    )

    def clean(self):
        regex_to_types = {
            "PHONE_NUMBER": r"(\(?\+)?(\(?[0-9-\s\.]\)?)+$",
            "EMAIL_ADDRESS": r".+@(([a-zA-Z0-9-])+\.)+([a-z])+$",
            "TELEGRAM_NICKNAME": r"(^(https://)?t\.me/)?[a-zA-Z0-9_]{5,}$",
            "LINKEDIN_ID": r"^((https://)?(www\.)?linkedin\.com/in/)?([a-zA-Z0-9-])+/?$",
        }
        if not re.fullmatch(regex_to_types[self.contact_type], self.value):
            raise forms.ValidationError("Incorrect Value")
        return self.value

    def __str__(self):
        return self.value

    __repr__ = __str__


class ContactTag(models.Model):
    tag = models.CharField("Tag", help_text="Name of contact tag", max_length=50)

    def __str__(self):
        return self.tag

    __repr__ = __str__


def get_icon_path(instance, filename: str) -> str:
    _, extension = filename.rsplit(".", maxsplit=1)
    return f"contacts/avatars/{instance.pk}/{uuid.uuid4()}/avatar.{extension}"


class Contact(models.Model):
    contact_name = models.CharField("Contact name", help_text="Name of contact", max_length=50)
    birthday = models.DateField("Birthday", help_text="Date of birth", null=True, blank=True)

    avatar = models.ImageField(
        "Avatar",
        upload_to=get_icon_path,
        max_length=255,
        blank=True,
        null=True,
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    contact_tags = models.ManyToManyField(ContactTag, related_name="contact_tags", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contact_name

    __repr__ = __str__
