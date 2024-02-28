import pymongo
from pymongo.mongo_client import MongoClient
from pymongo import collection
from pymongo import database
from pymongo.server_api import ServerApi
import os
import urllib.parse
from dotenv import load_dotenv

load_dotenv()


def mongo_client() -> MongoClient:
    db_user = os.getenv("DB_USER")
    db_pw = urllib.parse.quote_plus(os.getenv("DB_PASSWORD"))
    db_cluster = os.getenv("DB_CLUSTER")
    db_options = os.getenv("DB_OPTIONS")

    if os.getenv("DB_ENV") == "local":
        print(f"\n\nlocal database\n\n")
        db_client = MongoClient('localhost', 27017, uuidRepresentation='standard')
    else:
        print(f"\n\nremote database\n\n")
        uri = (f'mongodb+srv://{db_user}:{db_pw}'
               f'@{db_cluster}/'
               f'{db_options}')
        print(uri)
        db_client = MongoClient(uri, server_api=ServerApi('1'), uuidRepresentation='standard')

    try:
        db_client = db_client
        print(db_client)
        print(db_client.list_databases())
        return db_client
    except Exception as e:
        raise ConnectionError(str(e))


def ping_client(client: MongoClient):
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)


def set_db(client: MongoClient, db_name: str) -> database:
    db = client[db_name]
    print(db)
    return db


def set_collection(db: database, col_name: str) -> collection:
    col = db[col_name]
    print(col)
    return col


def close_client(client: MongoClient):
    print(f"\nClosing MongoDB Client\n")
    client.close()
