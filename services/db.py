import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.errors import OperationFailure
from pymongo import collection
from pymongo import database
from pymongo.server_api import ServerApi
from IPython.display import display_html, HTML
import os
import urllib.parse
from dotenv import load_dotenv

load_dotenv()


def mongo_client() -> MongoClient:
    db_user = os.getenv("DB_USER")
    db_pw = urllib.parse.quote_plus(os.getenv("DB_PASSWORD"))
    db_cluster = os.getenv("DB_CLUSTER")
    db_options = os.getenv("DB_OPTIONS")

    if os.getenv("DB_ENV") == "development":
        print(f"\nConnected using a local database\n")
        # db_client = MongoClient(f'admin:{db_pw}localhost', 27017, uuidRepresentation='standard')
        db_client = MongoClient( f"mongodb://{db_user}:{db_pw}@localhost:27017/")
    else:
        print(f"\nConnected using a remote database\n")
        uri = (f'mongodb+srv://{db_user}:{db_pw}'
               f'@{db_cluster}/'
               f'{db_options}')
        print(uri)
        db_client = MongoClient(uri, server_api=ServerApi('1'), uuidRepresentation='standard')

    try:
        db_client = db_client
        print(f"Client:\n{db_client}\n")
        databases = db_client.list_databases()
        print(f'Showing databases:')
        for db_object in databases:
            database_name = db_object['name']
            print(f'\tdatabase: {database_name}')
            try:
                col_names = db_client[database_name].list_collection_names()
                for col_name in col_names:
                    print(f'\t\t{col_name}{"\n" if len(col_names) - 1 == col_names.index(col_name) else ""}')

            except OperationFailure as e:
                collapsible_section = f"""
                    <details>
                        <summary>Permission to access collections in database \"{database_name}\" denied.</summary>
                        <p>{e}</p>
                    </details>
                    """
                display_html(HTML(collapsible_section))
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
