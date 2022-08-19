from django import forms

from apps.caesar.key_validator import KeyValidator


class EncryptForm(forms.Form):
    text_to_encrypt = forms.CharField(widget=forms.Textarea(attrs={"cols": 40, "rows": 2}), label="Text to Encrypt")
    key_to_encrypt = forms.IntegerField(label="Key to Encrypt", validators=[KeyValidator()])


class DecryptForm(forms.Form):
    text_to_decrypt = forms.CharField(widget=forms.Textarea(attrs={"cols": 40, "rows": 2}), label="Text to Decrypt")
    key_to_decrypt = forms.IntegerField(label="Key to Decrypt", validators=[KeyValidator(message="Decryption")])
