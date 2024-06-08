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
    def delete(self, conn, table_name):
        pass

    @abstractmethod
    def get_items(self, conn, table_name):
        pass

    @abstractmethod
    def insert(self, conn, link, model_name_id, table_name):
        pass

    def run_test(self, table_name):
        conn = self.get_connection()
        self.create_table(conn, table_name)
        conn.close()


class ThirdPageSqlite3Client(DataClient):
    DB_NAME = BASE_DIR / 'db.sqlite3'
    THIRD_PAGE_TABLE = 'av_app_thirdpage'

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
                    link text,
                    model_name_id bigint
                )
            """
        )
        conn.commit()

    def insert(self, conn, link, model_name_id, table_name):
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO {table_name} (link, model_name_id) VALUES ('{link}', '{model_name_id}')")
        conn.commit()

    def delete(self, conn, table_name):
        cursor = conn.cursor()
        cursor.execute(f'DELETE FROM {table_name}')
        conn.commit()

    def get_items(self, conn, table_name):
        cursor = conn.cursor()
        cursor.execute(f'SELECT id, link,  model_name_id FROM {table_name}')
        return cursor.fetchall()

