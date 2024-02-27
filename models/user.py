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
    """
    try:
        return helpers.validate_email_address(email)
    except ValueError as e:
        raise ValueError(f"Invalid email address: {str(e)}")


class User:
    def __init__(self,
                 uid: uuid.UUID = uuid.uuid4(),
                 email: str = None,
                 password: str = None):
        self.uid: uuid.UUID = uid
        self.created_at: datetime = datetime.now()
        self.email: str = validate_email(email)
        self.password: bytes = validate_password(password)

    def save(self, client: MongoClient) -> ObjectId:
        try:
            db = client[os.getenv("DATABASE")]
            col = db["users"]
            query_result = col.insert_one(self.__dict__)
            print(query_result)
            inserted_id = query_result.inserted_id
            return inserted_id
        except Exception as e:
            raise errors.PyMongoError(str(e))
