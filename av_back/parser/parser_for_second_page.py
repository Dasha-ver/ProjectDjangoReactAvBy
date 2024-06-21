from bs4 import BeautifulSoup
import requests
import second_page_data_client
import general_page_data_client


class ParserForSecondPage:
    general_page_data = general_page_data_client.GeneralPageSqlite3Client()
    general_page_list = general_page_data.get_items(general_page_data.get_connection(),
                                                    general_page_data.GENERAL_PAGE_TABLE)
    links_to_parse = []
    for item in general_page_list:
        links_to_parse.append(item[3])

    data_client_imp = second_page_data_client.SecondPageSqlite3Client()

    @staticmethod
    def get_second_page_by_link(link):
        mark_id = ''
        cookies = {
            'cf_clearance': '6YenUt_pzj120E72tLk0vj3QQjvNdLG3cR3N5tJrfws-1691757855-0-1-cffaf297.75aa331e.cac3e71-250.2.1691757855',
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        }

        response = requests.get(link, cookies=cookies, headers=headers)
        print(response)

        second_page_data = []
        bs = BeautifulSoup(response.text, "html.parser")
        general_page_data = general_page_data_client.GeneralPageSqlite3Client()
        general_page_list = general_page_data.get_items(general_page_data.get_connection(),
                                                        general_page_data.GENERAL_PAGE_TABLE)
        for gen_link in general_page_list:
            if gen_link[3] == link:
                mark_id = gen_link[0]

        for elem in bs.find_all('a', class_="catalog__link"):

            try:
                count = elem.text.replace(elem['title'], "").replace(")]", "")
                link = 'https://cars.av.by' + elem['href']
                second_page_data.append((
                    elem['title'],
                    int(count),
                    link,
                    mark_id

                ))
            except:
                print(f'Неполная информация. {elem.text}')
        return second_page_data

    def save_to_db(self, second_page_data):
        connection = self.data_client_imp.get_connection()
        self.data_client_imp.create_table(connection, second_page_data_client.SecondPageSqlite3Client.SECOND_PAGE_TABLE)
        for item in second_page_data:
            self.data_client_imp.insert(connection, item[0], item[1], item[2], item[3],
                                        second_page_data_client.SecondPageSqlite3Client.SECOND_PAGE_TABLE)

    def run(self):
        second_page_data = []
        for link in ParserForSecondPage.links_to_parse:
            second_page_data.extend(self.get_second_page_by_link(link))
        self.save_to_db(second_page_data)



