import pytest
from pytest_benchmark.fixture import BenchmarkFixture

from .services import encryptor, decryptor


@pytest.mark.parametrize(
    "input_text,key,output_text",
    [
        ("aaa", 2, "ccc"),
        ("AAA", 26, "aaa"),
        ("Ab c", 3, "de f"),
    ],
)
def test_encryption_good_benchmark(input_text: str, key: int, output_text: str, benchmark: BenchmarkFixture):
    result = benchmark(encryptor, input_text, key)
    assert result == output_text  # noqa: B101


@pytest.mark.parametrize(
    "input_text,key,output_text",
    [
        ("ccc", 2, "aaa"),
        ("AAA", 26, "aaa"),
        ("Ab c", 3, "xy z"),
    ],
)
def test_decryption_good(input_text: str, key: int, output_text: str):
    assert decryptor(input_text=input_text, key=key) == output_text  # noqa: B101


@pytest.mark.parametrize(
    "input_text,key",
    [
        ("aaa", -1),
    ],
)
def test_encryption_bad(input_text: str, key: int):
    with pytest.raises(ValueError):
        encryptor(input_text=input_text, key=key)


@pytest.mark.parametrize(
    "input_text,key",
    [
        ("aaa", -1),
    ],
)
def test_decryption_bad(input_text: str, key: int):
    with pytest.raises(ValueError):
        decryptor(input_text=input_text, key=key)
