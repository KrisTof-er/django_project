from django import forms


class EncryptForm(forms.Form):
    text_to_encrypt = forms.CharField(widget=forms.Textarea(attrs={"cols": 40, "rows": 2}), label="Text to Encrypt")
    key_to_encrypt = forms.IntegerField(min_value=0, label="Key to Encrypt")


class DecryptForm(forms.Form):
    text_to_decrypt = forms.CharField(widget=forms.Textarea(attrs={"cols": 40, "rows": 2}), label="Text to Decrypt")
    key_to_decrypt = forms.IntegerField(min_value=0, label="Key to Decrypt")
