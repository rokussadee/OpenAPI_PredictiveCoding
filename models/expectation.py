from typing import List
from bson.objectid import ObjectId
from pymongo import MongoClient, errors


class Expectation:
    def __init__(self,
                 reasoning: str,
                 user_predictions: List[str],
                 additional_data: List[str]):
        self.reasoning: str = reasoning
        self.user_predictions: List[str] = user_predictions
        self.additional_data: List[str] = additional_data

    def save(self, client: MongoClient) -> ObjectId:
        try:
            db = client[os.getenv("DATABASE")]
            col = db["expectations"]
            query_result = col.insert_one(self.__dict__)
            inserted_id = query_result.inserted_id
            return inserted_id
        except Exception as e:
            raise errors.PyMongoError(str(e))
