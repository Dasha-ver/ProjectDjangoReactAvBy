import sqlite3
from abc import ABC, abstractmethod
from sqlite3 import Error
from av_back.av_back.settings import BASE_DIR


class DataClient(ABC):

    @abstractmethod
    def get_connection(self):
        pass

    @abstractmethod
    def create_table(self, conn, table_name):
        pass

    @abstractmethod
    def insert(self, conn, rate, date, table_name):
        pass


class RateSqlite3Client(DataClient):
    DB_NAME = BASE_DIR / 'db.sqlite3'
    GENERAL_PAGE_TABLE = 'av_app_rate'

    def get_connection(self):
        try:
            conn = sqlite3.connect(self.DB_NAME)
            return conn
        except Error:
            print(Error)

    def create_table(self, conn, table_name):
        cursor_object = conn.cursor()
        cursor_object.execute(
            f"""
                CREATE TABLE IF NOT EXISTS {table_name}
                (
                    id integer PRIMARY KEY autoincrement, 
                    rate integer, 
                    date TEXT
                )
            """
        )
        conn.commit()

    def insert(self, conn, rate, date, table_name):
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO {table_name} (rate, date) VALUES ('{rate}', '{date}')")
        conn.commit()
