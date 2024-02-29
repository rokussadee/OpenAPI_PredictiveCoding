from datetime import datetime
from pymongo import MongoClient, errors
import os
from bson.objectid import ObjectId


class ChatbotResponse:
    """
    Represents a chatbot response.

    :param content: The content of the chatbot response.
    :param conversation_id: The ObjectId of the conversation this response belongs to.
    :param response_to_id: The ObjectId of the user message this response is in response to.
    """

    def __init__(self,
                 content: str,
                 conversation_id: ObjectId,
                 response_to_id: ObjectId):
        self.content: str = content
        self.created_at: datetime = created_at
        self.conversation_id: ObjectId = conversation_id
        self.response_to_id: ObjectId = response_to_id

    def save(self, client: MongoClient) -> ObjectId:
        """
        Saves a created ChatbotResponse instance into the MongoDB database.
        Raises a PyMongoError if the record could not be inserted into the database.

        :param client: The MongoDB client.
        :return: The MongoDB ObjectId of the saved chatbot response.
        """
        try:
            db = client[os.getenv("DATABASE")]
            col = db["chatbot_responses"]
            query_result = col.insert_one(self.__dict__)
            inserted_id = query_result.inserted_id
            return inserted_id
        except Exception as e:
            raise errors.PyMongoError(str(e))
