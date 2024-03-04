from typing import List
from datetime import datetime
from bson.objectid import ObjectId
from dataclasses import dataclass


@dataclass
class ExpectationRevisionData:
    created_at: datetime
    revised_input_possibilities: List[str]
    prediction_error: float
    initial_expectation_id: ObjectId


def create_expectation_revision(revised_input_possibilities: List[str],
                                prediction_error: float,
                                initial_expectation_id: ObjectId) -> ExpectationRevisionData:
    """
    Creates a dictionary containing expectation revision data.

    :param revised_input_possibilities: The revised input possibilities.
    :param prediction_error: The prediction error.
    :param initial_expectation_id: The ObjectId of the initial expectation object.
    :return: A dictionary containing expectation revision data.
    """
    return ExpectationRevisionData(
        datetime.now(),
        revised_input_possibilities,
        prediction_error,
        initial_expectation_id
    )

