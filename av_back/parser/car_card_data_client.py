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
    def delete(self, conn, table_name):
        pass

    @abstractmethod
    def get_each_mark_count(self, conn, table_name):
        pass

    @abstractmethod
    def get_each_model_count(self, conn, table_name):
        pass

    @abstractmethod
    def set_new_column(self, conn, table_name, column_name, datatype):
        pass

    @abstractmethod
    def get_column_data(self, conn, table_name, column_name):
        pass

    @abstractmethod
    def update_into_one_column(self, conn, table_name, column_name_for_set,
                               column_name_for_where, set_data, where_data):
        pass

    @abstractmethod
    def drop_column(self, conn, table_name, column_name):
        pass

    @abstractmethod
    def insert(self, conn, general_link, general_link_text, mark_link, mark_link_text, model_link, model_link_text,
               detailed_link, detailed_link_text, description_in_general, card_header, card_stat, card_price_primary,
               card_price_secondary, card_commercial, card_params, card_short_description, card_short_modification,
               card_all_param_button_href, card_location, vin, image_links, card_comment_text, card_exchange,
               exterior, security_systems, pillows, help_systems, interior, comfort, heating, climate, multimedia,
               headlights, card_finance_image, card_finance_description, card_finance_item_subtitle,
               card_average_price, card_average_price_description, first_similar_ad_photo, first_similar_ad_link,
               first_similar_ad_title, first_similar_ad_price, first_similar_ad_params, second_similar_ad_photo,
               second_similar_ad_link, second_similar_ad_title, second_similar_ad_price, second_similar_ad_params,
               third_similar_ad_photo, third_similar_ad_link, third_similar_ad_title, third_similar_ad_price,
               third_similar_ad_params, fourth_similar_ad_photo, fourth_similar_ad_link, fourth_similar_ad_title,
               fourth_similar_ad_price, fourth_similar_ad_params, fifth_similar_ad_photo, fifth_similar_ad_link,
               fifth_similar_ad_title, fifth_similar_ad_price, fifth_similar_ad_params, sixth_similar_ad_photo,
               sixth_similar_ad_link, sixth_similar_ad_title, sixth_similar_ad_price, sixth_similar_ad_params,
               seventh_similar_ad_photo, seventh_similar_ad_link, seventh_similar_ad_title, seventh_similar_ad_price,
               seventh_similar_ad_params, car_id, table_name):
        pass

    def run_test(self, table_name):
        conn = self.get_connection()
        self.create_table(conn, table_name)
        conn.close()


class CarSqlite3Client(DataClient):
    DB_NAME = BASE_DIR / 'db.sqlite3'
    CAR_PAGE_TABLE = 'av_app_car'

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
                    general_link text,
                    general_link_text text, 
                    mark_link text, 
                    mark_link_text text, 
                    model_link text,
                    model_link_text text, 
                    detailed_link text, 
                    detailed_link_text text, 
                    description_in_general text,
                    card_header text, 
                    card_stat text, 
                    card_price_primary integer, 
                    card_price_secondary integer, 
                    card_commercial text,
                    card_params text, 
                    card_short_description text, 
                    card_short_modification text, 
                    card_all_param_button_href text,
                    card_location text, 
                    vin text,
                    image_links text, 
                    card_comment_text text, 
                    card_exchange text, 
                    exterior text,
                    security_systems text, 
                    pillows text, 
                    help_systems text, 
                    interior text, 
                    comfort text, 
                    heating text, 
                    climate text,
                    multimedia text, 
                    headlights text, 
                    card_finance_image text, 
                    card_finance_description text,
                    card_finance_item_subtitle text, 
                    card_average_price text, 
                    card_average_price_description text,
                    first_similar_ad_photo text, 
                    first_similar_ad_link text, 
                    first_similar_ad_title text,
                    first_similar_ad_price text, 
                    first_similar_ad_params text, 
                    second_similar_ad_photo text,
                    second_similar_ad_link text, 
                    second_similar_ad_title text, 
                    second_similar_ad_price text,
                    second_similar_ad_params text, 
                    third_similar_ad_photo text, 
                    third_similar_ad_link text,
                    third_similar_ad_title text, 
                    third_similar_ad_price text, 
                    third_similar_ad_params text,
                    fourth_similar_ad_photo text, 
                    fourth_similar_ad_link text, 
                    fourth_similar_ad_title text,
                    fourth_similar_ad_price text, 
                    fourth_similar_ad_params text, 
                    fifth_similar_ad_photo text,
                    fifth_similar_ad_link text, 
                    fifth_similar_ad_title text, 
                    fifth_similar_ad_price text,
                    fifth_similar_ad_params text, 
                    sixth_similar_ad_photo text, 
                    sixth_similar_ad_link text,
                    sixth_similar_ad_title text, 
                    sixth_similar_ad_price text, 
                    sixth_similar_ad_params text,
                    seventh_similar_ad_photo text, 
                    seventh_similar_ad_link text, 
                    seventh_similar_ad_title text,
                    seventh_similar_ad_price text, 
                    seventh_similar_ad_params text,
                    car_id bigint
                )
            """
        )
        conn.commit()

    def insert(self, conn, general_link, general_link_text, mark_link, mark_link_text, model_link, model_link_text,
               detailed_link, detailed_link_text, description_in_general, card_header, card_stat, card_price_primary,
               card_price_secondary, card_commercial, card_params, card_short_description, card_short_modification,
               card_all_param_button_href, card_location, vin, image_links, card_comment_text, card_exchange,
               exterior, security_systems, pillows, help_systems, interior, comfort, heating, climate, multimedia,
               headlights, card_finance_image, card_finance_description, card_finance_item_subtitle,
               card_average_price, card_average_price_description, first_similar_ad_photo, first_similar_ad_link,
               first_similar_ad_title, first_similar_ad_price, first_similar_ad_params, second_similar_ad_photo,
               second_similar_ad_link, second_similar_ad_title, second_similar_ad_price, second_similar_ad_params,
               third_similar_ad_photo, third_similar_ad_link, third_similar_ad_title, third_similar_ad_price,
               third_similar_ad_params, fourth_similar_ad_photo, fourth_similar_ad_link, fourth_similar_ad_title,
               fourth_similar_ad_price, fourth_similar_ad_params, fifth_similar_ad_photo, fifth_similar_ad_link,
               fifth_similar_ad_title, fifth_similar_ad_price, fifth_similar_ad_params, sixth_similar_ad_photo,
               sixth_similar_ad_link, sixth_similar_ad_title, sixth_similar_ad_price, sixth_similar_ad_params,
               seventh_similar_ad_photo, seventh_similar_ad_link, seventh_similar_ad_title, seventh_similar_ad_price,
               seventh_similar_ad_params, car_id, table_name):
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO {table_name} (general_link, general_link_text, mark_link, mark_link_text, model_link, "
            f"model_link_text, detailed_link, detailed_link_text, description_in_general, card_header, card_stat,"
            f"card_price_primary, card_price_secondary, card_commercial, card_params, card_short_description,"
            f"card_short_modification, card_all_param_button_href, card_location, vin, image_links, card_comment_text,"
            f"card_exchange, exterior, security_systems, pillows, help_systems, interior, comfort, heating,"
            f"climate, multimedia, headlights, card_finance_image, card_finance_description, card_finance_item_subtitle,"
            f"card_average_price, card_average_price_description, first_similar_ad_photo, first_similar_ad_link,"
            f"first_similar_ad_title, first_similar_ad_price, first_similar_ad_params, second_similar_ad_photo,"
            f"second_similar_ad_link, second_similar_ad_title, second_similar_ad_price, second_similar_ad_params,"
            f"third_similar_ad_photo, third_similar_ad_link, third_similar_ad_title, third_similar_ad_price,"
            f"third_similar_ad_params, fourth_similar_ad_photo, fourth_similar_ad_link, fourth_similar_ad_title,"
            f"fourth_similar_ad_price, fourth_similar_ad_params, fifth_similar_ad_photo, fifth_similar_ad_link,"
            f"fifth_similar_ad_title, fifth_similar_ad_price, fifth_similar_ad_params, sixth_similar_ad_photo,"
            f"sixth_similar_ad_link, sixth_similar_ad_title, sixth_similar_ad_price, sixth_similar_ad_params,"
            f"seventh_similar_ad_photo, seventh_similar_ad_link, seventh_similar_ad_title, seventh_similar_ad_price,"
            f"seventh_similar_ad_params, car_id) VALUES ('{general_link}', '{general_link_text}', '{mark_link}',"
            f"'{mark_link_text}', '{model_link}',"
            f"'{model_link_text}', '{detailed_link}', '{detailed_link_text}', '{description_in_general}',"
            f"'{card_header}', '{card_stat}',"
            f"'{card_price_primary}', '{card_price_secondary}', '{card_commercial}', '{card_params}',"
            f"'{card_short_description}',"
            f"'{card_short_modification}', '{card_all_param_button_href}', '{card_location}', '{vin}', '{image_links}',"
            f"'{card_comment_text}',"
            f"'{card_exchange}', '{exterior}', '{security_systems}', '{pillows}', '{help_systems}', '{interior}', "
            f"'{comfort}', '{heating}',"
            f"'{climate}', '{multimedia}', '{headlights}', '{card_finance_image}', '{card_finance_description}', "
            f"'{card_finance_item_subtitle}',"
            f"'{card_average_price}', '{card_average_price_description}', '{first_similar_ad_photo}', "
            f"'{first_similar_ad_link}',"
            f"'{first_similar_ad_title}', '{first_similar_ad_price}', '{first_similar_ad_params}', "
            f"'{second_similar_ad_photo}',"
            f"'{second_similar_ad_link}', '{second_similar_ad_title}', '{second_similar_ad_price}', "
            f"'{second_similar_ad_params}',"
            f"'{third_similar_ad_photo}', '{third_similar_ad_link}', '{third_similar_ad_title}', "
            f"'{third_similar_ad_price}',"
            f"'{third_similar_ad_params}', '{fourth_similar_ad_photo}', '{fourth_similar_ad_link}', "
            f"'{fourth_similar_ad_title}',"
            f"'{fourth_similar_ad_price}', '{fourth_similar_ad_params}', '{fifth_similar_ad_photo}', "
            f"'{fifth_similar_ad_link}',"
            f"'{fifth_similar_ad_title}', '{fifth_similar_ad_price}', '{fifth_similar_ad_params}', "
            f"'{sixth_similar_ad_photo}',"
            f"'{sixth_similar_ad_link}', '{sixth_similar_ad_title}', '{sixth_similar_ad_price}', "
            f"'{sixth_similar_ad_params}',"
            f"'{seventh_similar_ad_photo}', '{seventh_similar_ad_link}', '{seventh_similar_ad_title}', "
            f"'{seventh_similar_ad_price}',"
            f"'{seventh_similar_ad_params}', '{car_id}')")
        conn.commit()

    def delete(self, conn, table_name):
        cursor = conn.cursor()
        cursor.execute(f'DELETE FROM {table_name}')
        conn.commit()

    def get_items(self, conn, table_name):
        cursor = conn.cursor()
        cursor.execute(f'SELECT mark_link FROM {table_name}')
        return cursor.fetchall()

    def get_each_mark_count(self, conn, table_name):
        cursor = conn.cursor()
        cursor.execute(f'SELECT mark_link,COUNT (*) FROM {table_name} GROUP BY mark_link')
        return cursor.fetchall()

    def get_each_model_count(self, conn, table_name):
        cursor = conn.cursor()
        cursor.execute(f'SELECT model_link,COUNT (*) FROM {table_name} GROUP BY model_link')
        return cursor.fetchall()

    def set_new_column(self, conn, table_name, column_name, datatype):
        cursor = conn.cursor()
        cursor.execute(f'ALTER TABLE {table_name} ADD COLUMN {column_name} {datatype}')
        conn.commit()

    def get_column_data(self, conn, table_name, column_name):
        cursor = conn.cursor()
        cursor.execute(f'SELECT {column_name} FROM {table_name}')
        return cursor.fetchall()

    def update_into_one_column(self, conn, table_name, column_name_for_set,
                               column_name_for_where, set_data, where_data):
        cursor = conn.cursor()
        cursor.execute(f'UPDATE {table_name} SET {column_name_for_set} = ? '
                       f'WHERE  {column_name_for_where} = ?', (set_data, where_data))
        conn.commit()

    def drop_column(self, conn, table_name, column_name):
        cursor = conn.cursor()
        cursor.execute(f'ALTER TABLE {table_name} DROP COLUMN {column_name}')
        conn.commit()
