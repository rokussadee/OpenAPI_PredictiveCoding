from email_validator import validate_email, EmailNotValidError
from password_validator import PasswordValidator
import bcrypt


def validate_email_address(email_address: str) -> str:
    """
    Validates an email address using the email_validator library.
    Raises EmailNotValidError if the email address is invalid.
    """
    try:
        email_object = validate_email(email_address)
        return email_object.normalized
    except EmailNotValidError as e:
        raise ValueError(str(e))


def validate_password(password: str) -> str:
    schema = PasswordValidator()
    schema \
        .min(8) \
        .max(25) \
        .has().uppercase() \
        .has().lowercase() \
        .has().digits() \
        .has().no().spaces()\

    try:
        schema.validate(password)
        return password
    except ValueError as e:
        raise ValueError(str(e))


def encrypt_password(password: str) -> bytes:
    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed


def check_password(hashed_password: bytes, stored_password: bytes) -> bool:
    is_same = bcrypt.checkpw(stored_password, hashed_password)
    return is_same
