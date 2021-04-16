from downloader import Downloader
from orebro import convert as convert_orebro
import os

from bs4 import BeautifulSoup

OREBRO_DOMAIN = 'https://www.orebro.se'
OREBRO_DATA_URL = '/fordjupning/fordjupning/fakta-statistik-priser--utmarkelser/information-tillganglig-for-ateranvandning/inkomna-leverantorsfakturor-reskontra--kontoklasser.html'


def get_orebro_file_list():
    soup = Downloader.get_html_soup(OREBRO_DOMAIN + OREBRO_DATA_URL)
    links = soup.find_all(
        lambda tag: tag.name == "a" and "Leverantörsfakturor" in tag.text)
    return [a['href'] for a in links]


links = get_orebro_file_list()

files = [
    'Leverant%C3%B6rsfakturor%202018.xlsx',
    'Leverant%C3%B6rsfakturor%202019.xlsx',
    'Leverant%C3%B6rsfakturor%202020.xlsx'
]

for link in links:
    url = OREBRO_DOMAIN + link
    #filename = Downloader.download_file(url)
    #files += [filename]

for filename in files:
    convert_orebro('./', './', os.path.splitext(filename)[0])
