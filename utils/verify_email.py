import re

pattern_for_valid_email = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?" \
                          r"(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"


class VerifyEmail:
    @staticmethod
    def verify(email):
        return bool(re.match(pattern_for_valid_email, email))
