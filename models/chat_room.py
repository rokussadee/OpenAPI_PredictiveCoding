from datetime import datetime
from typing import List

default_topic = ["New conversation topic"]


class ChatRoom:
    def __init__(self, user_name: str = "user",
                 user_message_count: int = 0,
                 user_login_count: int = 0,
                 conversation_topics: List[str] = None):
        """
        Represents a chat room.

        :param user_name: The name of the user.
        :param user_message_count: The count of user messages.
        :param user_login_count: The count of user logins.
        :param conversation_topics: List of conversation topics.
        """
        self.created_time: datetime = datetime.now()
        self.user_name: str = user_name
        self.user_message_count: int = user_message_count
        self.user_login_count: int = user_login_count
        self.conversation_topics: List[str] = conversation_topics if conversation_topics is not None else default_topic
