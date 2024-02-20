from datetime import datetime


class ChatRoom:
    def __init__(self, user_name: str = "user", user_message_count: int = 0, user_logins: int = 0):
        self.created_time = datetime.now()
        self.user_name = user_name
        self.user_message_count = user_message_count
        self.user_logins = user_logins
        self.conversation_topics = []
