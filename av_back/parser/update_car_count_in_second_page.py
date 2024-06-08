# Я создала этот класс для того, чтобы обновить данные в SECOND_PAGE_TABLE после того, как распарсила весь сайт

from car_card_data_client import CarSqlite3Client
from second_page_data_client import SecondPageSqlite3Client

second_page_data_client = SecondPageSqlite3Client()
car_data_client = CarSqlite3Client()
update_list = car_data_client.get_each_model_count(car_data_client.get_connection(), CarSqlite3Client.CAR_PAGE_TABLE)

second_page_data_client.update_count_to_null(second_page_data_client.get_connection(),
                                             SecondPageSqlite3Client.SECOND_PAGE_TABLE)

for item in update_list:
    second_page_data_client.update_count(second_page_data_client.get_connection(),
                                         SecondPageSqlite3Client.SECOND_PAGE_TABLE, item[1], item[0])

second_page_data_client.delete_if_count_zero(second_page_data_client.get_connection(),
                                             SecondPageSqlite3Client.SECOND_PAGE_TABLE)
