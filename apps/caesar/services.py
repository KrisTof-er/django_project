import string
from typing import Final

ALPHABET_CHARACTERS: Final[str] = string.ascii_lowercase


class NegativeValueError(Exception):
    def __init__(self):
        super().__init__("This value is less than 0")


def encryptor(input_text: str, key: int) -> str:
    if key < 0:
        raise NegativeValueError

    ALPHABET_REPEATS: Final[int] = key // len(ALPHABET_CHARACTERS) + 2
    ALPHABET: Final[str] = ALPHABET_CHARACTERS * ALPHABET_REPEATS

    input_text_lower = input_text.lower()
    encrypted_text = ""
    for letter in input_text_lower:
        index_in_alphabet = ALPHABET.find(letter)
        if index_in_alphabet == -1:
            encrypted_text += " "
        else:
            encrypted_text += ALPHABET[index_in_alphabet + key]
    return encrypted_text


def decryptor(input_text: str, key: int) -> str:
    if key < 0:
        raise NegativeValueError

    ALPHABET_REPEATS: Final[int] = key // len(ALPHABET_CHARACTERS) + 2
    ALPHABET: Final[str] = ALPHABET_CHARACTERS * ALPHABET_REPEATS

    input_text_lower = input_text.lower()
    decrypted_text = ""
    for letter in input_text_lower:
        index_in_alphabet = ALPHABET.find(letter)
        if index_in_alphabet == -1:
            decrypted_text += " "
        else:
            decrypted_text += ALPHABET[index_in_alphabet - key]
    return decrypted_text
