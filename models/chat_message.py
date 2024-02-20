from datetime import datetime


class ChatMessage:
    def __init__(self, author: str, content: str, chat_room: int):
        self.created_time = datetime.now()
        self.author = author
        self.content = content
        self.chat_room = chat_room
