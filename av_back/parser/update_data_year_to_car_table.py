#этот класс создан, чтобы создать колонку year в CAR_PAGE_TABLE и добавить туда данные из колонки card_params
from car_card_data_client import CarSqlite3Client

car_page_data_client = CarSqlite3Client()
car_page_data_client.set_new_column(car_page_data_client.get_connection(), CarSqlite3Client.CAR_PAGE_TABLE, 'year',
                                    'integer')

detailed_link_list = car_page_data_client.get_column_data(car_page_data_client.get_connection(),
                                                          CarSqlite3Client.CAR_PAGE_TABLE, 'card_params')
count = 0
for item in detailed_link_list:
    year = int(item[0].split(' ')[0])
    count += 1
    print(year, count)

    car_page_data_client.update_into_one_column(car_page_data_client.get_connection(),
                                                CarSqlite3Client.CAR_PAGE_TABLE, 'year', 'id',
                                                year, count)
