from datetime import datetime
from pymongo import collection, MongoClient, errors
from bson.objectid import ObjectId
import uuid
import os
from dotenv import load_dotenv
import utils.helpers as helpers

load_dotenv()


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


class User:
    def __init__(self,
                 uid: uuid.UUID = uuid.uuid4(),
                 email: str = None,
                 password: str = None):
        """
        Represents a user

        :param uid: The UUID of the user.
        :param email: The email address of the user.
        :param password: A sequence of bytes representing the password of the user.
        """
        self.uid: uuid.UUID = uid
        self.created_at: datetime = datetime.now()
        self.email: str = validate_email(email)
        self.password: bytes = validate_password(password)

    def save(self, client: MongoClient) -> ObjectId:
        """
        Saves a created User instance into the MongoDB database.
        Raises a PyMongoError if the record could not be inserted into the database.

        :param client: The MongoDB client.
        :return: The MongoDB ObjectId of the saved user.
        """
        try:
            db = client[os.getenv("DATABASE")]
            col = db["users"]
            query_result = col.insert_one(self.__dict__)
            print(query_result)
            inserted_id = query_result.inserted_id
            return inserted_id
        except Exception as e:
            raise errors.PyMongoError(str(e))
