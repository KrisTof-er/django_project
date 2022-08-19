from django.forms import ValidationError


class KeyValidator:
    message: str = "Encryption"

    def __init__(self, message=None):
        if message is not None:
            self.message = message

    def __call__(self, key):
        if key == 0:
            raise ValidationError(f"{self.message} operations with key=0 are useless")
