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
    def get_items(self, conn, table_name):
        pass

    @abstractmethod
    def insert(self, conn, title, count, link, table_name):
        pass

    @abstractmethod
    def update_count_to_null(self, conn, table_name):
        pass

    @abstractmethod
    def update_count(self, conn, table_name, count, link):
        pass

    @abstractmethod
    def delete_if_count_zero(self, conn, table_name):
        pass

    def run_test(self, table_name):
        conn = self.get_connection()
        self.create_table(conn, table_name)

        conn.close()


class GeneralPageSqlite3Client(DataClient):
    DB_NAME = BASE_DIR / 'db.sqlite3'
    GENERAL_PAGE_TABLE = 'av_app_generalpage'

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
                    title text, 
                    count integer, 
                    link text
                )
            """
        )
        conn.commit()

    def get_items(self, conn, table_name):
        cursor = conn.cursor()
        cursor.execute(f'SELECT id, title, count, link FROM {table_name}')
        return cursor.fetchall()

    def insert(self, conn, title, count, link, table_name):
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO {table_name} (title, count, link) VALUES ('{title}', '{count}', '{link}')")
        conn.commit()

    def update_count_to_null(self, conn, table_name):
        cursor = conn.cursor()
        cursor.execute(
            f"UPDATE {table_name} SET count = 0")
        conn.commit()

    def update_count(self, conn, table_name, count, link):
        cursor = conn.cursor()
        cursor.execute(
            f'UPDATE {table_name} SET count = ? WHERE link = ?', (count, link))
        conn.commit()

    def delete_if_count_zero(self, conn, table_name):
        cursor = conn.cursor()
        cursor.execute(
            f'DELETE FROM {table_name} WHERE count = 0')
        conn.commit()
