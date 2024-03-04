from datetime import datetime
from typing import List
from dataclasses import dataclass


@dataclass
class ExpectationData:
    created_at: datetime
    reasoning: str
    user_predictions: List[str]
    additional_data: List[str]


def create_expectation(reasoning: str, user_predictions: List[str], additional_data: List[str]) -> dict:
    """
    Creates a dictionary containing expectation data.

    :param reasoning: The reasoning behind the expectation.
    :param user_predictions: The predictions made by the user.
    :param additional_data: Additional data related to the expectation.
    :return: A dictionary containing expectation data.
    """
    return {"created_at": datetime.now(),
            "reasoning": reasoning,
            "user_predictions": user_predictions,
            "additional_data": additional_data}

