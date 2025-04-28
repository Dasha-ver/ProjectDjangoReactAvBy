from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re
import general_page_data_client


class ParserForGeneralPage:
    links_to_parse = ['https://av.by/', ]

    data_client_imp = general_page_data_client.GeneralPageSqlite3Client()

    @staticmethod
    def get_general_page_by_link(link):

        o = Options()
        o.add_experimental_option('detach', True)
        driver = webdriver.Chrome(options=o)

        driver.get(link)

        button = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/button[2]')
        button.click()

        button = driver.find_element(By.XPATH,
                                     '//*[@id="__next"]/div[2]/div[2]/div[1]/main/div/div/div/div[2]/div[1]/div['
                                     '2]/p/button')
        button.click()

        general_page_data = []
        source_data = driver.page_source
        bs = BeautifulSoup(source_data, 'html.parser')

        for elem in bs.find_all('a', class_="catalog__link"):
            try:
                title = ''.join(re.findall(r'[a-zA-Za-zA-Zа-яА-ЯёЁ()]+', elem.text))
                count = ''.join(re.findall(r'\d+', elem.text))
                general_page_data.append((
                    str(title),
                    int(count),
                    elem['href'],
                ))
            except:
                print(f'Неполная информация. {elem.text}')

        return general_page_data

    def save_to_db(self, general_page_data):
        connection = self.data_client_imp.get_connection()
        self.data_client_imp.create_table(connection, general_page_data_client.GeneralPageSqlite3Client().GENERAL_PAGE_TABLE)
        for item in general_page_data:
            self.data_client_imp.insert(connection, item[0], item[1], item[2],
                                        general_page_data_client.GeneralPageSqlite3Client().GENERAL_PAGE_TABLE)

    def run(self):
        general_page_data = []
        for link in ParserForGeneralPage.links_to_parse:
            general_page_data.extend(self.get_general_page_by_link(link))
        self.save_to_db(general_page_data)


