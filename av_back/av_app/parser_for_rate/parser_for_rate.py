from bs4 import BeautifulSoup
import requests
import datetime
from .rate_data_client import RateSqlite3Client


class ParserForRate:
    link_to_parse = "https://myfin.by/currency/usd"
    data_client_imp = RateSqlite3Client()

    @staticmethod
    def get_rate_by_link(link):

        response = requests.get(link)
        print(response)

        rate_data = []
        bs = BeautifulSoup(response.content, "html.parser")
        result = bs.find_all(class_="accent")
        try:
            rate = result[1].text
            date = datetime.date.today()
            rate_data.append((
                rate,
                date
            ))
        except:
            print(f'Неполная информация.')
        return rate_data

    def save_to_db(self, rate_data):
        connection = self.data_client_imp.get_connection()
        self.data_client_imp.create_table(connection, RateSqlite3Client.RATE_TABLE)
        for item in rate_data:
            self.data_client_imp.insert(connection, item[0], item[1],
                                        RateSqlite3Client.RATE_TABLE)

    def run(self):
        rate_data = []
        rate_data.extend(self.get_rate_by_link(ParserForRate.link_to_parse))
        self.save_to_db(rate_data)
