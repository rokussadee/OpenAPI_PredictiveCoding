from datetime import datetime
from pymongo import MongoClient, errors
import os
from bson.objectid import ObjectId


class ChatMessage:
    def __init__(self, user_id: ObjectId, content: str, conversation_id: ObjectId):
        """
        Represents a message in a chat room.

        :param user_id: The user_id of the user the message belongs to.
        :param content: The content of the message.
        :param conversation_id: The ID of the chat room to which the message belongs (foreign key to ChatRoom).
        """
        self.created_at: datetime = datetime.now()
        self.user_id: ObjectId = user_id
        self.content:  str = content
        self.conversation_id: ObjectId = conversation_id

    def save(self, client: MongoClient) -> ObjectId:
        """
        Saves a created ChatMessage instance into the MongoDB database.
        Raises a PyMongoError if the record could not be inserted into the database.

        :param client: The MongoDB client.
        :return: The MongoDB ObjectId of the saved chat_message.
        """
        try:
            db = client[os.getenv("DATABASE")]
            col = db["chat_messages"]
            query_result = col.insert_one(self.__dict__)
            print(query_result)
            inserted_id = query_result.inserted_id
            return inserted_id
        except Exception as e:
            raise errors.PyMongoError(str(e))
