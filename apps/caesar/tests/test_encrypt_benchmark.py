import pytest
from pytest_benchmark.fixture import BenchmarkFixture

from apps.caesar.services import encryptor


@pytest.mark.parametrize(
    "input_text,key,output_text",
    [
        ("aaa", 2, "ccc"),
        ("AAA;", 26, "AAA;"),
        ("Ab c", 3, "De f"),
    ],
)
def test_encryption_good_benchmark(input_text: str, key: int, output_text: str, benchmark: BenchmarkFixture):
    result = benchmark(encryptor, input_text, key)
    assert result == output_text  # noqa: B101
