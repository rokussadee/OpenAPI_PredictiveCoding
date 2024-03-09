from email_validator import validate_email, EmailNotValidError
from password_validator import PasswordValidator
from ipywidgets import Output as BaseOutput
import bcrypt
import os
from dotenv import load_dotenv

load_dotenv()
DEBUG_MODE = (os.getenv("DEBUG_MODE") == 'true')


def validate_email_address(email_address: str) -> str:
    """
    Validates an email address using the email_validator library.
    Raises EmailNotValidError if the email address is invalid.

    :param email_address: The email address to validate.
    :return: A string representing the email address validated and normalized by the email_validator library.
    """
    try:
        email_object = validate_email(email_address)
        return email_object.normalized
    except EmailNotValidError as e:
        raise ValueError(str(e))


def validate_password(password: str) -> str:
    """
    Validates the password based on the following criteria:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit

    :param password: The password to validate.
    :return: A string representing the password validated using the password validator_library.
    """
    schema = PasswordValidator()
    schema \
        .min(8) \
        .max(25) \
        .has().uppercase() \
        .has().lowercase() \
        .has().digits() \
        .has().no().spaces() \

    try:
        schema.validate(password)
        return password
    except ValueError as e:
        raise ValueError(str(e))


def encrypt_password(password: str) -> bytes:
    """
    Encrypts the provided password using the bcrypt library's "hashpw" method.

    :param password: The password to be encrypted using the bcrypt library.
    :return: A sequence of bytes representing the hashed password encrypted using the bcrypt library.
    """
    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed


def check_password(hashed_password: bytes, stored_password: bytes) -> bool:
    """
    Compares the provided hashed password with the corresponding user's password that was saved in the MongoDB database.

    :param hashed_password: A sequence of bytes representing the hashed password attempt that was provided by the user.
    :param stored_password: A sequence of bytes representing the hash of the stored password belonging to the user.
    :return: A boolean representing the result of the password comparison.
    """
    is_same = bcrypt.checkpw(stored_password, hashed_password)
    return is_same


class CustomOutput(BaseOutput):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def append_stdout(self, text, debug=False):
        if debug and not DEBUG_MODE:
            return
        if debug:
            text = "[DEBUG] " + text
        super().append_stdout(text)
