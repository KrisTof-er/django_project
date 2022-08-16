import pytest
from pytest_benchmark.fixture import BenchmarkFixture

from apps.caesar.services import encryptor


@pytest.mark.parametrize(
    "input_text,key,output_text,encryption_method",
    [
        ("aaa", 2, "ccc", True),
        ("AAA;", 26, "AAA;", True),
        ("Ab c", 3, "De f", True),
    ],
)
def test_encryption_good_benchmark(
    input_text: str, key: int, encryption_method: bool, output_text: str, benchmark: BenchmarkFixture
):
    result = benchmark(encryptor, input_text, key, encryption_method)
    assert result == output_text  # noqa: B101
