from pymongo.mongo_client import MongoClient
from pymongo.errors import OperationFailure
from pymongo import database, collection
from pymongo.server_api import ServerApi
from IPython.display import display_html, HTML
import os
import urllib.parse
from dotenv import load_dotenv

load_dotenv()


def mongo_client() -> MongoClient:
    """
    Initializes and returns a MongoClient instance for connecting to the MongoDB database.

    :returns: A MongoClient instance.
    """
    db_user = os.getenv("DB_USER")
    db_pw = urllib.parse.quote_plus(os.getenv("DB_PASSWORD"))
    db_cluster = os.getenv("DB_CLUSTER")
    db_options = os.getenv("DB_OPTIONS")

    print(f'Username: {db_user}, Password: {db_pw}')

    if os.getenv("DB_ENV") == "development":
        print(f"\nConnected using a local database\n")
        # db_client = MongoClient(f'admin:{db_pw}localhost', 27017, uuidRepresentation='standard')
        db_client = MongoClient( f"mongodb://{db_user}:{db_pw}@localhost:27017/")
        print(f"mongodb://{db_user}:{db_pw}@localhost:27017/")
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
    """
    Sends a ping command to the MongoDB client to confirm a successful connection.

    :param client: A MongoClient instance representing the MongoDB client.
    """

    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)


def set_db(client: MongoClient, db_name: str) -> database:
    """
    Sets the MongoDB database to be used.

    :param client: A MongoClient instance representing the MongoDB client.
    :param db_name: The name of the database to set.
    :returns: A pymongo.database.Database instance representing the selected database.
    """
    db = client[db_name]
    print(db)
    return db


def set_collection(db: database, col_name: str) -> collection:
    """
    Sets the MongoDB collection to be used within the selected database.

    :param db: A pymongo.database.Database instance representing the selected database.
    :param col_name: The name of the collection to set.
    :returns: A pymongo.collection.Collection instance representing the selected collection.
    """
    col = db[col_name]
    print(col)
    return col


def close_client(client: MongoClient):
    """
    Closes the MongoDB client connection.

    :param client: A MongoClient instance representing the MongoDB client.
    """
    print(f"\nClosing MongoDB Client\n")
    client.close()
