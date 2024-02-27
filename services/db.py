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
    mongo_user = os.getenv("MONGO_USER")
    mongo_pw = urllib.parse.quote_plus(os.getenv("MONGO_PASSWORD"))
    mongo_host = os.getenv("MONGO_HOST")
    mongo_port = os.getenv("MONGO_PORT")
    database = os.getenv("DATABASE")
    uri = (f'mongodb+srv://{mongo_user}:{mongo_pw}'
           f'@cluster.vfkvijy.mongodb.net/'
           f'?retryWrites=true'
           f'&w=majority'
           f'&appName=Cluster'
           f'&tlsCAFile=../isrgrootx1.pem')
    try:
        db_client = MongoClient(uri, server_api=ServerApi('1'), uuidRepresentation='standard')
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
