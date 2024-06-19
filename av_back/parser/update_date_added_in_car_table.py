# в процессе написания программы возникли проблемы из-за не совсем правильного парсинга сайта
# чтобы продемонстрировать возможность сортировки и добавления даты объявления, я добавила в таблицу
# CAR_PAGE_TABLE колонку с датой
# и добавила во все строки текущую дату. Удалила колонку card_state за ненадопностью.

import datetime
from car_card_data_client import CarSqlite3Client

car_page_data_client = CarSqlite3Client()
car_page_data_client.set_new_column(car_page_data_client.get_connection(), CarSqlite3Client.CAR_PAGE_TABLE,
                                    'date_added',
                                    'TEXT')

current_date = datetime.date.today()
cars_items = car_page_data_client.get_items(car_page_data_client.get_connection(), CarSqlite3Client.CAR_PAGE_TABLE)
count = 0

for item in cars_items:
    count += 1
    print(count)
    car_page_data_client.update_into_one_column(car_page_data_client.get_connection(), CarSqlite3Client.CAR_PAGE_TABLE,
                                                'date_added', 'id', current_date,
                                                count)

car_page_data_client.drop_column(car_page_data_client.get_connection(), CarSqlite3Client.CAR_PAGE_TABLE,
                                 'card_stat')

