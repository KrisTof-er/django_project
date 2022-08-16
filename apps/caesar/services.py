import string
from typing import Final

ALPHABET_LOWER: Final[str] = string.ascii_lowercase
ALPHABET_UPPER: Final[str] = string.ascii_uppercase


class NullValueError(Exception):
    def __init__(self):
        super().__init__("Encryption operations with key=0 are useless")


def encryptor(input_text: str, key: int, encryption_method: bool) -> str:
    if key == 0:
        raise NullValueError

    encryption_way = encryption_method and key > 0 or not encryption_method and key < 0

    if key < 0:
        key *= -1

    encrypted_text = ""
    for letter in input_text:
        index_in_alphabet = ALPHABET_UPPER.find(letter)
        if index_in_alphabet == -1:
            index_in_alphabet = ALPHABET_LOWER.find(letter)
            if index_in_alphabet == -1:
                encrypted_text += letter
            else:
                if encryption_way:
                    encrypted_text += ALPHABET_LOWER[index_in_alphabet + key % 26]
                else:
                    encrypted_text += ALPHABET_LOWER[index_in_alphabet - key % 26]
        else:
            if encryption_way:
                encrypted_text += ALPHABET_UPPER[index_in_alphabet + key % 26]
            else:
                encrypted_text += ALPHABET_UPPER[index_in_alphabet - key % 26]
    return encrypted_text
