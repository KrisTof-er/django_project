import pytest

from apps.caesar.services import encryptor, NullValueError

patterns = [
    ("ccc", -2, "aaa"),
    ("A/AA", -104, "A/AA"),
    ("De 0f", -3, "Ab 0c"),
]

patterns = [
    ("aaa", 2, "ccc"),
    ("A/AA", 104, "A/AA"),
    ("Ab c", 3, "De f"),
]


@pytest.mark.parametrize(
    "input_text,key,output_text",
    patterns,
)
def test_encryption_good(input_text: str, key: int, output_text: str):
    assert encryptor(input_text=input_text, key=key, encryption_method=True) == output_text  # noqa: B101


@pytest.mark.parametrize(
    "output_text,key,input_text",
    patterns,
)
def test_decryption_good(input_text: str, key: int, output_text: str):
    assert encryptor(input_text=input_text, key=key, encryption_method=False) == output_text  # noqa: B101


@pytest.mark.parametrize("input_text,key", [("aaa", "1")])
def test_encryption_bad__not_integer_value(input_text: str, key: int):
    with pytest.raises(TypeError):
        encryptor(input_text=input_text, key=key, encryption_method=True)


@pytest.mark.parametrize("input_text,key", [("aaa", 0)])
def test_encryption_bad__null_value(input_text: str, key: int):
    with pytest.raises(NullValueError):
        encryptor(input_text=input_text, key=key, encryption_method=True)
