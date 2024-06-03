from phone_normalizer.normalizer import PhoneNumberNormalizer

phone_numbers = [
    "+1 (234) 567-8901",
    "+44 123 456 7890",
    "+91-9876543210",
    "+86 10 12345678",
    "123-456-7890",
    "+49 (0) 30 1234567"
]

normalized_numbers = [PhoneNumberNormalizer.normalize(num) for num in phone_numbers]
print(normalized_numbers)
