# этот класс создан для обновления THIRD_PAGE_TABLE после удаления данных из других таблиц

from third_page_data_client import ThirdPageSqlite3Client
from second_page_data_client import SecondPageSqlite3Client

third_page_data = ThirdPageSqlite3Client()
second_page_data = SecondPageSqlite3Client()

third_page_data.delete_if_not_exist(third_page_data.get_connection(), ThirdPageSqlite3Client.THIRD_PAGE_TABLE,
                                    "model_name_id", SecondPageSqlite3Client.SECOND_PAGE_TABLE,
                                    "id")
