from datetime import datetime
from pymongo import MongoClient, errors
import os
from bson.objectid import ObjectId
from dataclasses import dataclass


@dataclass
class ChatMessageData:
    user_id: ObjectId
    content: str
    conversation_id: ObjectId


def create_chat_message(user_id: ObjectId, content: str, conversation_id: ObjectId) -> dict:
    """
    Creates a dictionary containing chat message data.

    :param user_id: The ObjectId of the user.
    :param content: The content of the message.
    :param conversation_id: The ObjectId of the conversation.
    :return: A dictionary containing chat message data.
    """
    return {"user_id": user_id, "content": content, "conversation_id": conversation_id}
