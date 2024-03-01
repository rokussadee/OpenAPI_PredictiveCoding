from typing import List
from bson.objectid import ObjectId
from pymongo import MongoClient, errors


class Expectation:
    def __init__(self,
                 reasoning: str,
                 user_predictions: List[str],
                 additional_data: List[str]):
        """
        Represents an expectation object.

        :param reasoning: Reasoning about the user’s internal mental state.
        :param user_predictions: Likely possibilities for the next user input.
        :param additional_data: A list of any additional data that would be useful to improve the prediction.
        """
        self.reasoning: str = reasoning
        self.user_predictions: List[str] = user_predictions
        self.additional_data: List[str] = additional_data

    def save(self, client: MongoClient) -> ObjectId:
        """
        Saves a created Expectation instance into the MongoDB database.
        Raises a PyMongoError if the record could not be inserted into the database.

        :param client: The MongoDB client.
        :return: The MongoDB ObjectId of the saved expectation.
        """
        try:
            db = client[os.getenv("DATABASE")]
            col = db["expectations"]
            query_result = col.insert_one(self.__dict__)
            inserted_id = query_result.inserted_id
            return inserted_id
        except Exception as e:
            raise errors.PyMongoError(str(e))
