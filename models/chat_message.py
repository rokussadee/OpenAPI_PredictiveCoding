from datetime import datetime


class ChatMessage:
    def __init__(self, author: str, content: str, conversation_id: int):
        """
        Represents a message in a chat room.

        :param author: The author of the message.
        :param content: The content of the message.
        :param conversation_id: The ID of the chat room to which the message belongs (foreign key to ChatRoom).
        """
        self.created_time: datetime = datetime.now()
        self.author: str = author
        self.content:str = content
        self.conversation_id:int = conversation_id
