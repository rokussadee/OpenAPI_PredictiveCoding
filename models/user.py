from datetime import datetime
from pymongo import collection, MongoClient, errors
from bson.objectid import ObjectId
import uuid
import os
from dotenv import load_dotenv
import utils.helpers as helpers
from dataclasses import dataclass

load_dotenv()


@dataclass
class UserData:
    email: str
    password: str


def validate_email(email: str) -> str:
    """
    Validates the email address using the helper function.
    Raises a ValueError if the email is not valid.
    :param email: The email address to validate
    :return: The validated email address
    """
    try:
        return helpers.validate_email_address(email)
    except ValueError as e:
        raise ValueError(f"Invalid email address: {str(e)}")


def validate_password(password: str) -> bytes:
    """
    Validates the password using the helper function.
    Raises a ValueError if the password is not valid.

    :param password: The password to validate.
    :return: The validated password encrypted using a helper function.
    """
    try:
        validated_password = helpers.validate_password(password)
        return helpers.encrypt_password(validated_password)
    except ValueError as e:
        raise ValueError(f"Invalid password: {str(e)}")


def create_user_data(email: str, password: str) -> dict:
    """
    Creates a dictionary containing user data.

    :param email: The email address of the user.
    :param password: The password of the user.
    :return: A dictionary containing user data if the password is valid, otherwise None.
    """
    validated_password = validate_password(password)
    validated_email = validate_email(email)

    return {"email": validated_email, "password": validated_password}
