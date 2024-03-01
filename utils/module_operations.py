from pymongo import MongoClient, errors
from bson.objectid import ObjectId
import os
from models.user import UserData
from models.conversation import ConversationData
from models.chat_message import ChatMessageData
from models.violation import ViolationData
from models.expectation import ExpectationData
from models.expectation_revision import ExpectationRevisionData
from models.chatbot_response import ChatbotResponseData
from typing import Dict, Type

COLLECTION_DATA_CLASS_MAP: Dict[str, Type] = {
    'users': UserData,
    'conversations': ConversationData,
    'chat_messages': ChatMessageData,
    'violations': ViolationData,
    'expectations': ExpectationData,
    'expectation_revisions': ExpectationRevisionData,
    'chatbot_responses': ChatbotResponseData
}


def create_model(collection_name: str, model_data: dict, client: MongoClient) -> ObjectId:
    """
    Creates a new model instance and saves it to the specified collection in the MongoDB database.

    :param collection_name: The name of the collection in which to save the model.
    :param model_data: A dictionary representing the model data to be saved.
    :param client: The MongoDB client.
    :return: The MongoDB ObjectId of the saved model.
    """

    if collection_name not in COLLECTION_DATA_CLASS_MAP:
        raise ValueError(f"No data class defined for collection: {collection_name}")

    data_class = COLLECTION_DATA_CLASS_MAP[collection_name]
    if not isinstance(model_data, data_class):
        raise ValueError(f"model_data must be of type {data_class.__name__}")

    try:
        db = client[os.getenv("DATABASE")]
        col = db[collection_name]
        query_result = col.insert_one(model_data.__dict__)
        inserted_id = query_result.inserted_id
        return inserted_id
    except Exception as e:
        raise errors.PyMongoError(str(e))


def get_model(collection, model_id, client: MongoClient):
    """
    Retrieves a model instance from the specified collection in the MongoDB database.

    :param collection: The name of the collection from which to retrieve the model.
    :param model_id: The ObjectId of the model to retrieve.
    :param client: The MongoDB client.
    :return: A dictionary representing the retrieved model instance.
    """
    try:
        db = client[os.getenv("DATABASE")]
        col = db[collection]
        model = col.find_one({"_id": ObjectId(model_id)})
        return model
    except Exception as e:
        raise errors.PyMongoError(str(e))


def update_model(collection, model_id, update_data, client: MongoClient):
    """
    Updates a model instance in the specified collection in the MongoDB database.

    :param collection: The name of the collection containing the model to update.
    :param model_id: The ObjectId of the model to update.
    :param update_data: A dictionary containing the updated data for the model.
    :param client: The MongoDB client.
    """
    try:
        db = client[os.getenv("DATABASE")]
        col = db[collection]
        col.update_one({"_id": ObjectId(model_id)}, {"$set": update_data})
    except Exception as e:
        raise errors.PyMongoError(str(e))


def delete_model(collection, model_id, client: MongoClient):
    """
    Deletes a model instance from the specified collection in the MongoDB database.

    :param collection: The name of the collection containing the model to delete.
    :param model_id: The ObjectId of the model to delete.
    :param client: The MongoDB client.
    """
    try:
        db = client[os.getenv("DATABASE")]
        col = db[collection]
        col.delete_one({"_id": ObjectId(model_id)})
    except Exception as e:
        raise errors.PyMongoError(str(e))
