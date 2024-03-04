from datetime import datetime
from bson.objectid import ObjectId
from dataclasses import dataclass
from typing import Optional


@dataclass
class ViolationData:
    created_at: datetime
    last_llm_response_id: Optional[ObjectId]
    expectation_id: ObjectId
    voe_thought: str


def create_violation(last_llm_response_id: Optional[ObjectId], expectation_id: ObjectId, voe_thought: str) -> dict:
    """
    Creates a dictionary containing violation data.

    :param last_llm_response_id: The ObjectId of the last LLM (Language Learning Model) response.
    :param expectation_id: The ObjectId of the expectation object.
    :param voe_thought: The content of the violation.
    :return: A dictionary containing violation data.
    """
    return {"created_at": datetime.now(),
            "last_llm_response_id": last_llm_response_id,
            "expectation_id": expectation_id,
            "voe_thought": voe_thought}

