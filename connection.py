import os
from dotenv import load_dotenv
from pymongo import MongoClient
from sqlalchemy import create_engine

class DatabaseConnector:
    def __init__(self):
        load_dotenv()

        self.mongo_uri = os.getenv("MONGO_URI")
        self.mongo_database = os.getenv("MONGO_DATABASE")
        self.mongo_collection = os.getenv("MONGO_COLLECTION")

        self.sql_username = os.getenv("SQL_USERNAME")
        self.sql_password = os.getenv("SQL_PASSWORD")
        self.sql_database = os.getenv("SQL_DATABASE")
        self.sql_table = os.getenv("SQL_TABLE")
        self.sql_host = os.getenv("SQL_HOST")
        self.sql_port = os.getenv("SQL_PORT")

        self.sql_engine = create_engine(
            f"postgresql://{self.sql_username}:{self.sql_password}@{self.sql_host}:{self.sql_port}/{self.sql_database}"
        )

    def get_mongo_connection(self):
        client = MongoClient(self.mongo_uri)
        return client[self.mongo_database]

    def get_sql_connection(self):
        return self.sql_engine

if __name__ == "__main__":
    db = DatabaseConnector()
    mongo_db = db.get_mongo_connection()
    sql_engine = db.get_sql_connection()
    print("MongoDB ve PostgreSQL bağlantıları başarıyla kuruldu.")
