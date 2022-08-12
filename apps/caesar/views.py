from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from apps.caesar.forms import EncryptForm, DecryptForm
from apps.caesar.services import encryptor, decryptor


def encrypt_or_decrypt(request: HttpRequest) -> HttpResponse:
    encrypted_text = ""
    decrypted_text = ""
    if request.method == "POST" and "encryptbtn" in request.POST:
        form_encrypt = EncryptForm(request.POST)
        form_decrypt = DecryptForm()
        if form_encrypt.is_valid():
            encrypted_text = encryptor(
                input_text=form_encrypt.data["text_to_encrypt"], key=int(form_encrypt.data["key_to_encrypt"])
            )
    elif request.method == "POST" and "decryptbtn" in request.POST:
        form_encrypt = EncryptForm()
        form_decrypt = DecryptForm(request.POST)
        if form_decrypt.is_valid():
            decrypted_text = decryptor(
                input_text=form_decrypt.data["text_to_decrypt"], key=int(form_decrypt.data["key_to_decrypt"])
            )
    else:
        form_encrypt = EncryptForm()
        form_decrypt = DecryptForm()
    return render(
        request,
        "caesar/caesar_cipher.html",
        {
            "form_encrypt": form_encrypt,
            "form_decrypt": form_decrypt,
            "encrypted_text": encrypted_text,
            "decrypted_text": decrypted_text,
        },
    )
