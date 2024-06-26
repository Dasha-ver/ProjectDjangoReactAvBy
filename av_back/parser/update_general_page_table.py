# обновление значений MercedesBenz, AlfaRomeo, DongfengHonda, Lada(ВАЗ), GreatWall,  LandRover.
# вставка пробела между словами, чтобы фильтрация по значению осуществлялась корректно

from general_page_data_client import GeneralPageSqlite3Client
import re

general_page_data_client = GeneralPageSqlite3Client()

update_list = ['MercedesBenz', 'AlfaRomeo', 'DongfengHonda', 'Lada(ВАЗ)', 'GreatWall', 'LandRover']

for item in update_list:
    print(re.sub(r"(\w)([A-Z (\s])", r"\1 \2", item))
    general_page_data_client.update_line(general_page_data_client.get_connection(),
                                         GeneralPageSqlite3Client.GENERAL_PAGE_TABLE, 'title', 'title',
                                         re.sub(r"(\w)([A-Z (\s])", r"\1 \2", item), item)
general_page_data_client.update_line(general_page_data_client.get_connection(),
                                     GeneralPageSqlite3Client.GENERAL_PAGE_TABLE, 'title', 'title',
                                     'Mercedes-Benz', 'Mercedes Benz')
