# Я создала этот класс для того, чтобы обновить данные в GENERAL_PAGE_TABLE после того, как распарсила весь сайт

from car_card_data_client import CarSqlite3Client
from general_page_data_client import GeneralPageSqlite3Client

general_page_data_client = GeneralPageSqlite3Client()
car_data_client = CarSqlite3Client()
update_list = car_data_client.get_each_mark_count(car_data_client.get_connection(), CarSqlite3Client.CAR_PAGE_TABLE)

general_page_data_client.update_count_to_null(general_page_data_client.get_connection(),
                                              GeneralPageSqlite3Client.GENERAL_PAGE_TABLE)
for item in update_list:
    general_page_data_client.update_count(general_page_data_client.get_connection(),
                                          GeneralPageSqlite3Client.GENERAL_PAGE_TABLE, item[1], item[0])

general_page_data_client.delete_if_count_zero(general_page_data_client.get_connection(),
                                              GeneralPageSqlite3Client.GENERAL_PAGE_TABLE)


