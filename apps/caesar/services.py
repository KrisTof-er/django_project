import string
from typing import Final

ALPHABET_LOWER: Final[str] = string.ascii_lowercase
ALPHABET_UPPER: Final[str] = string.ascii_uppercase


class NegativeValueError(Exception):
    def __init__(self):
        super().__init__("This value is less than 0")


def encryptor(input_text: str, key: int) -> str:
    if key < 0:
        raise NegativeValueError

    encrypted_text = ""
    for letter in input_text:
        index_in_alphabet = ALPHABET_UPPER.find(letter)
        if index_in_alphabet == -1:
            index_in_alphabet = ALPHABET_LOWER.find(letter)
            if index_in_alphabet == -1:
                encrypted_text += letter
            else:
                encrypted_text += ALPHABET_LOWER[index_in_alphabet + key % 26]
        else:
            encrypted_text += ALPHABET_UPPER[index_in_alphabet + key % 26]
    return encrypted_text


def decryptor(input_text: str, key: int) -> str:
    if key < 0:
        raise NegativeValueError

    encrypted_text = ""
    for letter in input_text:
        index_in_alphabet = ALPHABET_UPPER.find(letter)
        if index_in_alphabet == -1:
            index_in_alphabet = ALPHABET_LOWER.find(letter)
            if index_in_alphabet == -1:
                encrypted_text += letter
            else:
                encrypted_text += ALPHABET_LOWER[index_in_alphabet - key % 26]
        else:
            encrypted_text += ALPHABET_UPPER[index_in_alphabet - key % 26]
    return encrypted_text
