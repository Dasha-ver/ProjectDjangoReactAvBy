from bs4 import BeautifulSoup
import requests
import third_page_data_client
import car_card_data_client
import re


class ParserForCarCard:
    third_page_data = third_page_data_client.ThirdPageSqlite3Client()
    third_page_list = third_page_data.get_items(third_page_data.get_connection(),
                                                third_page_data.THIRD_PAGE_TABLE)
    links_to_parse = []
    for item in third_page_list[57000:57500]:
        links_to_parse.append(item[1])

    data_client_imp = car_card_data_client.CarSqlite3Client()

    @staticmethod
    def get_car_options(car_options_data):

        car_options = []
        for i in car_options_data:
            car_options.append(i.text)
        options = ', '.join(car_options)
        return options

    @staticmethod
    def get_car_card_by_link(link):

        cookies = {
            'cf_clearance': '6YenUt_pzj120E72tLk0vj3QQjvNdLG3cR3N5tJrfws-1691757855-0-1-cffaf297.75aa331e.cac3e71-250.2.1691757855',
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        }

        response = requests.get(link, cookies=cookies, headers=headers)
        print(response)

        car_id = ' '
        car_card_data = []
        general_links_data = []
        image_links_data = []
        bs = BeautifulSoup(response.text, "html.parser")

        third_page_data_for_get = third_page_data_client.ThirdPageSqlite3Client()
        third_page_list_for_get = third_page_data_for_get.get_items(third_page_data_for_get.get_connection(),
                                                                    third_page_data_for_get.THIRD_PAGE_TABLE)
        for car_link in third_page_list_for_get:
            if car_link[1] == link:
                car_id = car_link[0]

        for elem in bs.find_all('div', class_='layout__content overlay-container'):
            for general in elem.find_all('a'):
                try:

                    general_links_data.append((
                        general['href'],
                        general['title']
                    ))
                except:
                    print(f'Неполная информация. {elem.text}')

            try:
                general_link = 'https://cars.av.by'
                general_link_text = general_links_data[0][1]
                mark_link = 'https://cars.av.by' + general_links_data[1][0]
                mark_link_text = general_links_data[1][1]
                model_link = 'https://cars.av.by' + general_links_data[2][0]
                model_link_text = general_links_data[2][1]
                detailed_link = 'https://cars.av.by' + general_links_data[3][0]
                detailed_link_text = general_links_data[3][1]
                description_in_general = elem.find_all('span', attrs={'itemprop': 'name'})[5].text
                card_header = re.sub(r'[^\x00-\x7fа-яА-Я]', ' ', elem.find('h1', class_='card__title').text)
                card_stat = elem.find('ul', class_='card__stat').text.replace('№', ' №').replace('0', '')
                card_price_primary = re.sub(r'[^\x00-\x7f]|[\W]', '',
                                            elem.find('div', class_='card__price-primary').text)
                card_price_secondary = re.sub(r'[^\x00-\x7f]|[\W]', '',
                                              elem.find('div', class_='card__price-secondary').text)
                card_commercial = re.sub(r'[^\x00-\x7fА-Яа-я]', ' ',
                                         elem.find('div', class_='card__commercial').text)
                card_params = re.sub(r'[^\x00-\x7fА-Яа-я]', ' ', elem.find('div', class_='card__params').text)
                card_short_description = elem.find('div', class_='card__description').text
                card_short_modification = elem.find('div', class_='card__modification').text.replace(
                    'Все параметры',
                    '')
                card_all_param_button_href = elem.find_all('a')[4]
                card_location = elem.find('div', 'card__location').text
                vin = elem.find('b').text
                for item in elem.find_all('div', class_='gallery__nav-frame'):
                    for link in item.find_all('img'):
                        image_links_data.append(
                            link['data-src']
                        )
                image_links = ', '.join(image_links_data)
                card_comment_text = re.sub(r'[^\x00-\x7fА-Яа-я]|[^"\\]', ' ', elem.find('div', 'card__comment-text').text)
                card_exchange = elem.find('div', 'card__exchange').text
                car_options = elem.find_all('ul', class_='card__options-list')
                exterior = ParserForCarCard.get_car_options(car_options[0])
                security_systems = ParserForCarCard.get_car_options(car_options[1])
                pillows = ParserForCarCard.get_car_options(car_options[2])
                help_systems = ParserForCarCard.get_car_options(car_options[3])
                interior = ParserForCarCard.get_car_options(car_options[4])
                comfort = ParserForCarCard.get_car_options(car_options[5])
                heating = ParserForCarCard.get_car_options(car_options[6])
                climate = ParserForCarCard.get_car_options(car_options[7])
                multimedia = ParserForCarCard.get_car_options(car_options[8])
                headlights = ParserForCarCard.get_car_options(car_options[9])
                card_finance_image = elem.find('img', class_='card-finance__image')['src']
                card_finance_description = re.sub(r'[^\x00-\x7fа-яА-Я]', ' ',
                                                  elem.find('p', class_='card-finance__description').text)
                card_finance_item_subtitle = re.sub(r'[^\x00-\x7fа-яА-Я]', ' ', elem.find('span', class_='finance'
                                                                                                         '-item__subtitle').text)
                card_average_price = re.sub(r'[^\x00-\x7f$]', '', elem.find('div',
                                                                            class_='featured__price-value').text)
                card_average_price_description = re.sub(r'[^\x00-\x7fа-яА-Я]', ' ',
                                                        elem.find('div', class_='featured__price-description').text)
                similar_ads_photos = elem.find_all('div', class_='listing-top__photo')
                similar_ads_links = elem.find_all('a', class_='listing-top__title-link')
                similar_ads_titles = elem.find_all('span', class_='link-text')
                similar_ads_prices = elem.find_all('div', class_='listing-top__price')
                similar_ads_params = elem.find_all('div', class_='listing-top__params')
                first_similar_ad_photo = similar_ads_photos[0].find('img', class_='lazyload')['data-src']
                first_similar_ad_link = 'https://cars.av.by' + similar_ads_links[0]['href']
                first_similar_ad_title = similar_ads_titles[4].text
                first_similar_ad_price = re.sub(r'[^\x00-\x7fа-яА-Я$]', ' ', similar_ads_prices[0].text)
                first_similar_ad_params = re.sub(r'[^\x00-\x7fа-яА-Я]', ' ', similar_ads_params[0].text)
                second_similar_ad_photo = similar_ads_photos[1].find('img', class_='lazyload')['data-src']
                second_similar_ad_link = 'https://cars.av.by' + similar_ads_links[1]['href']
                second_similar_ad_title = similar_ads_titles[5].text
                second_similar_ad_price = re.sub(r'[^\x00-\x7fа-яА-Я$]', ' ', similar_ads_prices[1].text)
                second_similar_ad_params = re.sub(r'[^\x00-\x7fа-яА-Я]', ' ', similar_ads_params[1].text)
                third_similar_ad_photo = similar_ads_photos[2].find('img', class_='lazyload')['data-src']
                third_similar_ad_link = 'https://cars.av.by' + similar_ads_links[2]['href']
                third_similar_ad_title = similar_ads_titles[6].text
                third_similar_ad_price = re.sub(r'[^\x00-\x7fа-яА-Я$]', ' ', similar_ads_prices[2].text)
                third_similar_ad_params = re.sub(r'[^\x00-\x7fа-яА-Я]', ' ', similar_ads_params[2].text)
                fourth_similar_ad_photo = similar_ads_photos[3].find('img', class_='lazyload')['data-src']
                fourth_similar_ad_link = 'https://cars.av.by' + similar_ads_links[3]['href']
                fourth_similar_ad_title = similar_ads_titles[7].text
                fourth_similar_ad_price = re.sub(r'[^\x00-\x7fа-яА-Я$]', ' ', similar_ads_prices[3].text)
                fourth_similar_ad_params = re.sub(r'[^\x00-\x7fа-яА-Я]', ' ', similar_ads_params[3].text)
                fifth_similar_ad_photo = similar_ads_photos[4].find('img', class_='lazyload')['data-src']
                fifth_similar_ad_link = 'https://cars.av.by' + similar_ads_links[4]['href']
                fifth_similar_ad_title = similar_ads_titles[8].text
                fifth_similar_ad_price = re.sub(r'[^\x00-\x7fа-яА-Я$]', ' ', similar_ads_prices[4].text)
                fifth_similar_ad_params = re.sub(r'[^\x00-\x7fа-яА-Я]', ' ', similar_ads_params[4].text)
                sixth_similar_ad_photo = similar_ads_photos[5].find('img', class_='lazyload')['data-src']
                sixth_similar_ad_link = 'https://cars.av.by' + similar_ads_links[5]['href']
                sixth_similar_ad_title = similar_ads_titles[9].text
                sixth_similar_ad_price = re.sub(r'[^\x00-\x7fа-яА-Я$]', ' ', similar_ads_prices[5].text)
                sixth_similar_ad_params = re.sub(r'[^\x00-\x7fа-яА-Я]', ' ', similar_ads_params[5].text)
                seventh_similar_ad_photo = similar_ads_photos[6].find('img', class_='lazyload')['data-src']
                seventh_similar_ad_link = 'https://cars.av.by' + similar_ads_links[6]['href']
                seventh_similar_ad_title = similar_ads_titles[10].text
                seventh_similar_ad_price = re.sub(r'[^\x00-\x7fа-яА-Я$]', ' ', similar_ads_prices[6].text)
                seventh_similar_ad_params = re.sub(r'[^\x00-\x7fа-яА-Я]', ' ', similar_ads_params[6].text)
                car_card_data.append((
                    general_link,
                    general_link_text,
                    mark_link,
                    mark_link_text,
                    model_link,
                    model_link_text,
                    detailed_link,
                    detailed_link_text,
                    description_in_general,
                    card_header,
                    card_stat,
                    int(card_price_primary),
                    int(card_price_secondary),
                    card_commercial,
                    card_params,
                    card_short_description,
                    card_short_modification,
                    card_all_param_button_href['href'],
                    card_location,
                    vin,
                    str(image_links),
                    card_comment_text,
                    card_exchange,
                    str(exterior),
                    str(security_systems),
                    str(pillows),
                    str(help_systems),
                    str(interior),
                    str(comfort),
                    str(heating),
                    str(climate),
                    str(multimedia),
                    str(headlights),
                    card_finance_image,
                    card_finance_description,
                    card_finance_item_subtitle,
                    card_average_price,
                    card_average_price_description,
                    first_similar_ad_photo,
                    first_similar_ad_link,
                    first_similar_ad_title,
                    first_similar_ad_price,
                    first_similar_ad_params,
                    second_similar_ad_photo,
                    second_similar_ad_link,
                    second_similar_ad_title,
                    second_similar_ad_price,
                    second_similar_ad_params,
                    third_similar_ad_photo,
                    third_similar_ad_link,
                    third_similar_ad_title,
                    third_similar_ad_price,
                    third_similar_ad_params,
                    fourth_similar_ad_photo,
                    fourth_similar_ad_link,
                    fourth_similar_ad_title,
                    fourth_similar_ad_price,
                    fourth_similar_ad_params,
                    fifth_similar_ad_photo,
                    fifth_similar_ad_link,
                    fifth_similar_ad_title,
                    fifth_similar_ad_price,
                    fifth_similar_ad_params,
                    sixth_similar_ad_photo,
                    sixth_similar_ad_link,
                    sixth_similar_ad_title,
                    sixth_similar_ad_price,
                    sixth_similar_ad_params,
                    seventh_similar_ad_photo,
                    seventh_similar_ad_link,
                    seventh_similar_ad_title,
                    seventh_similar_ad_price,
                    seventh_similar_ad_params,
                    car_id

                ))
            except:
                print(f'Неполная информация. {elem.text}')
        print(car_card_data)
        return car_card_data

    def save_to_db(self, car_card_data):
        connection = self.data_client_imp.get_connection()
        self.data_client_imp.create_table(connection, car_card_data_client.CarSqlite3Client.CAR_PAGE_TABLE)
        for item in car_card_data:
            self.data_client_imp.insert(connection, item[0], item[1], item[2], item[3], item[4], item[5],
                                        item[6], item[7], item[8], item[9], item[10], item[11], item[12],
                                        item[13], item[14], item[15], item[16], item[17], item[18], item[19],
                                        item[20], item[21], item[22], item[23], item[24], item[25], item[26],
                                        item[27], item[28], item[29], item[30], item[31], item[32], item[33],
                                        item[34], item[35], item[36], item[37], item[38], item[39], item[40],
                                        item[41], item[42], item[43], item[44], item[45], item[46], item[47],
                                        item[48], item[49], item[50], item[51], item[52], item[53], item[54],
                                        item[55], item[56], item[57], item[58], item[59], item[60], item[61],
                                        item[62], item[63], item[64], item[65], item[66], item[67], item[68],
                                        item[69], item[70], item[71], item[72], item[73],
                                        car_card_data_client.CarSqlite3Client.CAR_PAGE_TABLE)
        print('Добавлено')

    def run(self):
        car_card_data = []
        for link in ParserForCarCard.links_to_parse:
            car_card_data.extend(self.get_car_card_by_link(link))
        self.save_to_db(car_card_data)


# print(ParserForCarCard.get_car_card_by_link(link='https://cars.av.by/abarth/124-spider/108394958'))

# print(ParserForCarCard.get_car_card_by_link(link='https://cars.av.by/jaguar/f-pace/101374771'))
# third_page_data = third_page_data_client.ThirdPageSqlite3Client()
# third_page_list = third_page_data.get_items(third_page_data.get_connection(),
#                                             third_page_data.THIRD_PAGE_TABLE)
# links_to_parse = []
# for item in third_page_list[:1]:
#     links_to_parse.append(item[1])
#
# print(links_to_parse)
# d = ParserForCarCard.get_car_card_by_link(link='https://cars.av.by/jaguar/f-pace/101374771')
#
# for item in d:
#     print(item[8])