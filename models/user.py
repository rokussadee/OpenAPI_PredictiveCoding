from datetime import datetime
import uuid
import utils.helpers as helpers


def validate_email(email: str) -> str:
    """
    Validates the email address using the helper function.
    Raises a ValueError if the email is not valid.
    """
    try:
        return helpers.validate_email_address(email)
    except ValueError as e:
        raise ValueError(f"Invalid email address: {str(e)}")


class User:
    def __init__(self,
                 uid: uuid.UUID = uuid.uuid4(),
                 email: str = None):
        self.uid: uuid.UUID = uid
        self.email: str = validate_email(email)
