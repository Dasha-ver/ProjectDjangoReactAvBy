from bs4 import BeautifulSoup
import requests


def p():
    URL = "https://myfin.by/currency/usd"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find_all(class_="accent")
    print(result[1].text)
