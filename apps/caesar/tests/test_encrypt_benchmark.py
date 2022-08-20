import pytest
from pytest_benchmark.fixture import BenchmarkFixture

from apps.caesar.services import encryptor
from apps.caesar.tests.test_encrypt_decrypt import patterns


@pytest.mark.parametrize(
    "input_text,key,output_text",
    patterns,
)
def test_encryption_good_benchmark(input_text: str, key: int, output_text: str, benchmark: BenchmarkFixture):
    result = benchmark(encryptor, input_text, key)
    assert result == output_text  # noqa: B101
