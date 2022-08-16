import pytest

from apps.caesar.services import encryptor, decryptor, NegativeValueError

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
    assert encryptor(input_text=input_text, key=key) == output_text  # noqa: B101


@pytest.mark.parametrize(
    "output_text,key,input_text",
    patterns,
)
def test_decryption_good(input_text: str, key: int, output_text: str):
    assert decryptor(input_text=input_text, key=key) == output_text  # noqa: B101


@pytest.mark.parametrize("input_text,key", [("aaa", "1")])
def test_encryption_bad__not_integer_value(input_text: str, key: int):
    with pytest.raises(TypeError):
        encryptor(input_text=input_text, key=key)


@pytest.mark.parametrize("input_text,key", [("aaa", -1)])
def test_encryption_bad__negative_value(input_text: str, key: int):
    with pytest.raises(NegativeValueError):
        encryptor(input_text=input_text, key=key)


@pytest.mark.parametrize("input_text,key", [("aaa", "1")])
def test_decryption_bad__not_integer_value(input_text: str, key: int):
    with pytest.raises(TypeError):
        decryptor(input_text=input_text, key=key)


@pytest.mark.parametrize("input_text,key", [("aaa", -1)])
def test_decryption_bad__negative_value(input_text: str, key: int):
    with pytest.raises(NegativeValueError):
        decryptor(input_text=input_text, key=key)
