import re


class PhoneNumberNormalizer:
    COUNTRY_CODE_LENGTHS = {"+1": 10, "+44": 10, "+91": 10, "+86": 11, "+49": 10}

    @classmethod
    def normalize(cls, phone_number: str) -> str:
        cleaned_number = re.sub(r"[ \-\(\)]", "", phone_number)

        if not re.match(r"^\+\d+", cleaned_number):
            return "Invalid"

        for country_code in cls.COUNTRY_CODE_LENGTHS.keys():
            if cleaned_number.startswith(country_code):
                number_length = cls.COUNTRY_CODE_LENGTHS[country_code]
                local_number = cleaned_number[len(country_code) :]
                if len(local_number) == number_length:
                    return cleaned_number
                else:
                    return "Invalid"

        return "Invalid"
