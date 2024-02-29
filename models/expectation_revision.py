from typing import List
from pymongo import MongoClient, errors
from bson.objectid import ObjectId


class ExpectationRevision:
    def __init__(self,
                 revised_input_possibilities: List[str],
                 prediction_error: float,
                 initial_expectation_id: ObjectId):
        self.revised_input_possibilities: List[str] = revised_input_possibilities
        self.prediction_error: float= prediction_error
        self.initial_expectation_id: ObjectId = initial_expectation_id

    def save(self, client: MongoClient) -> ObjectId:
        try:
            db = client[os.getenv("DATABASE")]
            col = db["expectation_revisions"]
            query_result = col.insert_one(self.__dict__)
            inserted_id = query_result.inserted_id
            return inserted_id
        except Exception as e:
            raise errors.PyMongoError(str(e))