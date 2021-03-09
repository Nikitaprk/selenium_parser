from bs4 import BeautifulSoup
import requests

url = 'https://edadeal.ru/sankt-peterburg/offers?segment=alcohol'
headers = {
    "Accept": "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 OPR/74.0.3911.160"
}


def get_html(url, params=''):
    req = requests.Session()
    smt = req.get(url, headers=headers, params=params)
    return smt


src = get_html(url).text
print(get_html(url))
soup = BeautifulSoup(src, 'html5lib')
quotes = soup.find_all('title', class_='b-offer__description')
print(quotes)
print(src)
