from typing import List
from pymongo import MongoClient, errors
from bson.objectid import ObjectId


class Violation:
    def __init__(self,
                 last_llm_response_id: ObjectId,
                 expectation_id: ObjectId,
                 voe_thought: str):
        self.last_llm_response_id: ObjectId = last_llm_response_id
        self.expectation_id: ObjectId = expectation_id
        self.voe_thought: str = voe_thought

    def save(self, client: MongoClient) -> ObjectId:
        try:
            db = client[os.getenv("DATABASE")]
            col = db["violations"]
            query_result = col.insert_one(self.__dict__)
            inserted_id = query_result.inserted_id
            return inserted_id
        except Exception as e:
            raise errors.PyMongoError(str(e))
