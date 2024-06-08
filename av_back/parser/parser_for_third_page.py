from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import third_page_data_client
import second_page_data_client


class ParserForThirdPage:
    second_page_data = second_page_data_client.SecondPageSqlite3Client()
    second_page_list = second_page_data.get_items(second_page_data.get_connection(),
                                                  second_page_data.SECOND_PAGE_TABLE)
    links_to_parse = []
    for item in second_page_list:
        links_to_parse.append(item[3])

    data_client_imp = third_page_data_client.ThirdPageSqlite3Client()

    @staticmethod
    def get_third_page_by_link(link):
        model_name_id = ' '
        driver = webdriver.Chrome()

        driver.get(link)
        button = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/button[2]')
        button.click()

        try:
            button = driver.find_element(By.XPATH,
                                         '//*[@id="__next"]/div[2]/main/div/div/div[1]/div[5]/div[3]/div/div[4]/div/div['
                                         '1]/a')

            while button.is_displayed():
                button.click()
        except:
            print("На странице менее 25 элементов")

        third_page_data = []
        source_data = driver.page_source
        bs = BeautifulSoup(source_data, 'html.parser')

        second_page_data = second_page_data_client.SecondPageSqlite3Client()
        second_page_list = second_page_data.get_items(second_page_data.get_connection(),
                                                      second_page_data.SECOND_PAGE_TABLE)
        for second_link in second_page_list:
            if second_link[3] == link:
                model_name_id = second_link[0]

        for elem in bs.find_all('a', class_="listing-item__link"):
            try:
                link = 'https://cars.av.by' + elem['href']
                third_page_data.append((
                    link,
                    model_name_id
                ))
            except:
                print(f'Неполная информация. {elem.text}')

        return third_page_data

    def save_to_db(self, third_page_data):
        connection = self.data_client_imp.get_connection()
        self.data_client_imp.create_table(connection, third_page_data_client.ThirdPageSqlite3Client.THIRD_PAGE_TABLE)
        for item in third_page_data:
            self.data_client_imp.insert(connection, item[0], item[1],
                                        third_page_data_client.ThirdPageSqlite3Client.THIRD_PAGE_TABLE)
        print('Добавлено')

    def run(self):
        third_page_data = []
        for link in ParserForThirdPage.links_to_parse:
            third_page_data.extend(self.get_third_page_by_link(link))
        self.save_to_db(third_page_data)




# print(ParserForThirdPage.get_third_page_by_link(link='https://cars.av.by/audi/a5'))
# second_page_data = second_page_data_client.SecondPageSqlite3Client()
# second_page_list = second_page_data.get_items(second_page_data.get_connection(),
#                                                   second_page_data.SECOND_PAGE_TABLE)
# links_to_parse = []
# for item in second_page_list:
#     links_to_parse.append(item[3])
# print(links_to_parse)
# second_page_data = second_page_data_client.SecondPageSqlite3Client()
# second_page_list = second_page_data.get_items(second_page_data.get_connection(),
#                                                   second_page_data.SECOND_PAGE_TABLE)
# links_to_parse = []
# for item in second_page_list[:20]:
#     links_to_parse.append(item[3])
# print(links_to_parse)
