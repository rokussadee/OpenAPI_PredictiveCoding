from datetime import datetime
from pymongo import MongoClient, errors
import os
from bson.objectid import ObjectId


class ChatbotResponse:
    def __init__(self,
                 content: str,
                 created_at: datetime,
                 conversation_id: ObjectId,
                 response_to_id: ObjectId):
        self.content: str = content
        self.created_at: datetime = created_at
        self.conversation_id: ObjectId = conversation_id
        self.response_to_id: ObjectId = response_to_id

    def save(self, client: MongoClient) -> ObjectId:
        try:
            db = client[os.getenv("DATABASE")]
            col = db["chatbot_responses"]
            query_result = col.insert_one(self.__dict__)
            inserted_id = query_result.inserted_id
            return inserted_id
        except Exception as e:
            raise errors.PyMongoError(str(e))
