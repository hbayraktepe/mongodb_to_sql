import pandas as pd
import logging
from connection import DatabaseConnector

logging.basicConfig(filename='data_transfer.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


class DataTransfer:
    def __init__(self):
        self.db = DatabaseConnector()
        self.mongo_db = self.db.get_mongo_connection()
        self.sql_engine = self.db.get_sql_connection()

    def transfer_data(self):
        try:
            data = self.mongo_db[self.db.mongo_collection].find()
            df = pd.DataFrame(list(data))

            df['_id'] = df['_id'].astype(str)

            df.to_sql(name=self.db.sql_table, con=self.sql_engine, if_exists='append', index=False)
            logging.info("Data successfully transferred to PostgreSQL.")
        except Exception as e:
            logging.error(f"An error occurred: {e}")


if __name__ == '__main__':
    transfer = DataTransfer()
    transfer.transfer_data()
