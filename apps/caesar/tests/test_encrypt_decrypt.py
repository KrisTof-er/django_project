import pytest

from apps.caesar.services import encryptor, NullValueError

patterns = [
    ("ccc", -2, "aaa"),
    ("A/AA", -104, "A/AA"),
    ("De 0f", -3, "Ab 0c"),
    ("HellO, 573 Worlds!", -104, "HellO, 573 Worlds!"),
]


@pytest.mark.parametrize(
    "input_text,key,output_text",
    patterns,
)
def test_encryption_decryption_good(input_text: str, key: int, output_text: str):
    encrypted_text = encryptor(input_text=input_text, key=key)
    assert encryptor(input_text=encrypted_text, key=key, is_encrypt=False) == input_text  # noqa: B101


@pytest.mark.parametrize(
    "input_text,key,output_text",
    patterns,
)
def test_encryption_good(input_text: str, key: int, output_text: str):
    assert encryptor(input_text=input_text, key=key) == output_text  # noqa: B101


@pytest.mark.parametrize(
    "output_text,key,input_text",
    patterns,
)
def test_decryption_good(input_text: str, key: int, output_text: str):
    assert encryptor(input_text=input_text, key=key, is_encrypt=False) == output_text  # noqa: B101


@pytest.mark.parametrize("input_text,key", [("aaa", "1")])
def test_encryption_bad__not_integer_value(input_text: str, key: int):
    with pytest.raises(TypeError):
        encryptor(input_text=input_text, key=key)


@pytest.mark.parametrize("input_text,key", [("aaa", 0)])
def test_encryption_bad__null_value(input_text: str, key: int):
    with pytest.raises(NullValueError):
        encryptor(input_text=input_text, key=key)
