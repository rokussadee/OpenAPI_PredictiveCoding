from datetime import datetime
from typing import List
from bson.objectid import ObjectId
from dataclasses import dataclass

default_topic = ["New conversation topic"]


@dataclass
class ConversationData:
    created_at: datetime
    user_id: ObjectId
    user_message_count: int = 0
    user_login_count: int = 0
    conversation_topics: List[str] = None


def create_conversation(user_id: ObjectId, user_message_count: int = 0, user_login_count: int = 0, conversation_topics: List[str] = None) -> ConversationData:
    """
    Creates a dictionary containing conversation data.

    :param user_id: The ObjectId of the user.
    :param user_message_count: The count of messages in the conversation.
    :param user_login_count: The count of logins in the conversation.
    :param conversation_topics: The topics of the conversation.
    :return: A dictionary containing conversation data.
    """
    if conversation_topics is None:
        conversation_topics = []
    return ConversationData(
        datetime.now(),
        user_id,
        user_message_count,
        user_login_count,
        conversation_topics
    )
