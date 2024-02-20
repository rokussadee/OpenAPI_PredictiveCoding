from datetime import datetime


class ChatRoom:
    def __init__(self, user_name="user", user_message_count=0, user_logins=0):
        self.created_time = datetime.now()
        self.user_name = user_name
        self.user_message_count = user_message_count
        self.user_logins = user_logins
        self.conversation_topics = []
