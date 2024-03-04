from typing import List
from pymongo import MongoClient, errors
from bson.objectid import ObjectId


@dataclass
class ExpectationRevisionData:
    revised_input_possibilities: List[str]
    prediction_error: float
    initial_expectation_id: ObjectId


def create_expectation_revision(revised_input_possibilities: List[str],
                                prediction_error: float,
                                initial_expectation_id: ObjectId) -> dict:
    """
    Creates a dictionary containing expectation revision data.

    :param revised_input_possibilities: The revised input possibilities.
    :param prediction_error: The prediction error.
    :param initial_expectation_id: The ObjectId of the initial expectation object.
    :return: A dictionary containing expectation revision data.
    """
    return {"created_at": datetime.now(),
            "revised_input_possibilities": revised_input_possibilities,
            "prediction_error": prediction_error,
            "initial_expectation_id": initial_expectation_id}

