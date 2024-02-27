from datetime import datetime
from typing import List
import uuid

default_topic = ["New conversation topic"]


class Conversation:
    def __init__(self, user_uid: uuid.UUID,
                 user_message_count: int = 0,
                 user_login_count: int = 0,
                 conversation_topics: List[str] = None):
        """
        Represents a conversation.

        :param user_uid: The UUID of the user that has initiated this conversation.
        :param user_message_count: The count of messages sent by the user in this conversation (excluding bot messages).
        :param user_login_count: The count of user logins.
        :param conversation_topics: List of conversation topics.
        """
        self.created_at: datetime = datetime.now()
        self.user_uid: uuid.UUID = user_uid
        self.user_message_count: int = user_message_count
        self.user_login_count: int = user_login_count
        self.conversation_topics: List[str] = conversation_topics if conversation_topics is not None else default_topic
