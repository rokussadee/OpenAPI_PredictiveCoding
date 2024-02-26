from email_validator import validate_email, EmailNotValidError


def validate_email_address(email_address: str) -> str:
    """
    Validates an email address using the email_validator library.
    Returns the normalized email address if valid.
    Raises EmailNotValidError if the email address is invalid.
    """
    try:
        email_object = validate_email(email_address)
        return email_object.normalized
    except EmailNotValidError as e:
        raise ValueError(str(e))
