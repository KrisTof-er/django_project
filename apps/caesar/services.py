import string
from typing import Final

# ALPHABET: Final[str] = string.ascii_lowercase
# ALPHABET_UPPER: Final[str] = string.ascii_uppercase
# ALPHABET_LENGTH: Final[int] = len(ALPHABET_UPPER)
# NOT_FOUND_CHARACTER_IDENTIFIER: Final[int] = ALPHABET.find(f"{ALPHABET_UPPER} ")

ALPHABET: Final[str] = string.ascii_lowercase
ALPHABET_UPPER: Final[str] = ALPHABET.upper()
ALPHABET_LENGTH: Final[int] = len(ALPHABET)
NOT_FOUND_CHARACTER_IDENTIFIER: Final[int] = -1


class NullValueError(Exception):
    def __init__(self):
        super().__init__("Encryption operations with key=0 are useless")


def encryptor(input_text: str, key: int, is_encrypt: bool = True) -> str:
    if key == 0:
        raise NullValueError

    is_encrypt = is_encrypt and key > 0 or not is_encrypt and key < 0

    if key < 0:
        key *= -1

    encrypted_text = ""
    for letter in input_text:
        index_in_alphabet = ALPHABET_UPPER.find(letter)
        if index_in_alphabet == NOT_FOUND_CHARACTER_IDENTIFIER:
            index_in_alphabet = ALPHABET.find(letter)
            if index_in_alphabet == NOT_FOUND_CHARACTER_IDENTIFIER:
                encrypted_text += letter
            else:
                if is_encrypt:
                    encrypted_text += ALPHABET[(index_in_alphabet + key) % ALPHABET_LENGTH]
                else:
                    encrypted_text += ALPHABET[(index_in_alphabet - key) % ALPHABET_LENGTH]
        else:
            if is_encrypt:
                encrypted_text += ALPHABET_UPPER[(index_in_alphabet + key) % ALPHABET_LENGTH]
            else:
                encrypted_text += ALPHABET_UPPER[(index_in_alphabet - key) % ALPHABET_LENGTH]
    return encrypted_text
