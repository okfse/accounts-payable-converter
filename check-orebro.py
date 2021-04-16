import html
import urllib.request
import os
from bs4 import BeautifulSoup

OREBRO_DOMAIN = 'https://www.orebro.se'
OREBRO_DATA_URL = '/fordjupning/fordjupning/fakta-statistik-priser--utmarkelser/information-tillganglig-for-ateranvandning/inkomna-leverantorsfakturor-reskontra--kontoklasser.html'


def get(url):
    try:
        return urllib.request.urlopen(url).read()
    except urllib.error.HTTPError as err:
        print(f'ERROR {err.code}: Could not download {url}.')


response = get(OREBRO_DOMAIN + OREBRO_DATA_URL)

htmlData = html.unescape(response.decode('utf-8'))
soup = BeautifulSoup(htmlData, 'html.parser')
links = soup.find_all(
    lambda tag: tag.name == "a" and "Leverantörsfakturor" in tag.text)
links = [a['href'] for a in links]

for link in links:
    url = OREBRO_DOMAIN + link
    filename = os.path.basename(url)
    urllib.request.urlretrieve(url, filename)
    print('\Successfully downloaded ' + filename)
