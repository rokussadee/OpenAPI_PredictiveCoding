from typing import List
from pymongo import MongoClient, errors
from bson.objectid import ObjectId


class Violation:
    def __init__(self,
                 last_llm_response_id: ObjectId,
                 expectation_id: ObjectId,
                 voe_thought: str):
        """
        Represents a violation object.

        :param last_llm_response_id: The ObjectId of the last LLM (Language Learning Model) response.
        :param expectation_id: The ObjectId of the expectation object.
        :param voe_thought: The content of the violation.
        """
        self.last_llm_response_id: ObjectId = last_llm_response_id
        self.expectation_id: ObjectId = expectation_id
        self.voe_thought: str = voe_thought

    def save(self, client: MongoClient) -> ObjectId:
        """
        Saves a created Violation instance into the MongoDB database.
        Raises a PyMongoError if the record could not be inserted into the database.

        :param client: The MongoDB client.
        :return: The MongoDB ObjectId of the saved violation.
        """
        try:
            db = client[os.getenv("DATABASE")]
            col = db["violations"]
            query_result = col.insert_one(self.__dict__)
            inserted_id = query_result.inserted_id
            return inserted_id
        except Exception as e:
            raise errors.PyMongoError(str(e))
