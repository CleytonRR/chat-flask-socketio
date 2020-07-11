from werkzeug.security import generate_password_hash, check_password_hash


class PasswordHash:

    @staticmethod
    def encrypted_password(password):
        return generate_password_hash(password)

    @staticmethod
    def verify_password(encrypted_password, password):
        return check_password_hash(encrypted_password, password)