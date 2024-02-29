from typing import List
from pymongo import MongoClient, errors
from bson.objectid import ObjectId


class ExpectationRevision:
    def __init__(self,
                 revised_input_possibilities: List[str],
                 prediction_error: float,
                 initial_expectation_id: ObjectId):
        """
        Represents an expectation revision object.

        :param revised_input_possibilities: The revised input possibilities.
        :param prediction_error: The prediction error.
        :param initial_expectation_id: The ObjectId of the initial expectation object.
        """
        self.revised_input_possibilities: List[str] = revised_input_possibilities
        self.prediction_error: float= prediction_error
        self.initial_expectation_id: ObjectId = initial_expectation_id

    def save(self, client: MongoClient) -> ObjectId:
        """
        Saves a created ExpectationRevision instance into the MongoDB database.
        Raises a PyMongoError if the record could not be inserted into the database.

        :param client: The MongoDB client.
        :return: The MongoDB ObjectId of the saved expectation revision.
        """
        try:
            db = client[os.getenv("DATABASE")]
            col = db["expectation_revisions"]
            query_result = col.insert_one(self.__dict__)
            inserted_id = query_result.inserted_id
            return inserted_id
        except Exception as e:
            raise errors.PyMongoError(str(e))