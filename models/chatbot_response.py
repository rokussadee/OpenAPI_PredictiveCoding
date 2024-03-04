from datetime import datetime
from bson.objectid import ObjectId


@dataclass
class ChatbotResponseData:
    created_at: datetime
    content: str
    conversation_id: ObjectId
    response_to_id: ObjectId


def create_chatbot_response(content: str, conversation_id: ObjectId, response_to_id: ObjectId) -> dict:
    """
    Creates a dictionary containing chatbot response data.

    :param content: The content of the response.
    :param conversation_id: The ObjectId of the conversation.
    :param response_to_id: The ObjectId of the response to which this response is replying.
    :return: A dictionary containing chatbot response data.
    """
    return {"created_at": datetime.now(),
            "content": content,
            "conversation_id": conversation_id,
            "response_to_id": response_to_id}
