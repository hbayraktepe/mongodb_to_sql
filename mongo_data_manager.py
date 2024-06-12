from datetime import datetime
from connection import DatabaseConnector
import pymongo

class MongoDBManager:
    def __init__(self):
        db_connector = DatabaseConnector()
        self.mongo_db = db_connector.get_mongo_connection()
        self.collection = self.mongo_db[db_connector.mongo_collection]
        self.entry_number = self.initialize_entry_number()

    def initialize_entry_number(self):
        try:
            latest_entry = self.collection.find_one(sort=[('entry_number', pymongo.DESCENDING)])
            if latest_entry and 'entry_number' in latest_entry:
                return latest_entry['entry_number'] + 1
            else:
                return 1
        except Exception as e:
            print(f"Entry number initialize error: {e}")
            return 1

    def add_data(self):
        data = {}
        print("Veri eklemek için bilgileri girin (bitirmek için 'done' yazın):")
        while True:
            field = input("Alan adı: ")
            if field.lower() == 'done':
                break
            value = input(f"{field} için değer: ")
            data[field] = value

        data['entry_date'] = datetime.now().isoformat()
        data['entry_number'] = self.entry_number
        self.entry_number += 1

        try:
            result = self.collection.insert_one(data)
            print(f"Veri başarıyla eklendi, Document ID: {result.inserted_id}")
        except Exception as e:
            print(f"Veri ekleme sırasında hata oluştu: {e}")

if __name__ == '__main__':
    manager = MongoDBManager()
    manager.add_data()
