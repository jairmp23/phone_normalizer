import pytest
from phone_normalizer.normalizer import PhoneNumberNormalizer

@pytest.mark.parametrize("phone_number, expected", [
    ("+1 (234) 567-8901", "+12345678901"),
    ("+44 123 456 7890", "+441234567890"),
    ("+91-9876543210", "+919876543210"),
    ("+86 10 12345678", "Invalid"),
    ("123-456-7890", "Invalid"),
    ("+23 123-456-7890", "Invalid"),
    ("+49 (0) 30 1234567", "+490301234567")
])
def test_normalize(phone_number, expected):
    assert PhoneNumberNormalizer.normalize(phone_number) == expected
