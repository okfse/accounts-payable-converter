import html
import urllib.request
import os

from bs4 import BeautifulSoup


class Downloader(object):
    @staticmethod
    def get(url):
        try:
            return urllib.request.urlopen(url).read()
        except urllib.error.HTTPError as err:
            print(f'ERROR {err.code}: Could not download {url}.')

    @staticmethod
    def get_html_soup(url):
        response = Downloader.get(url)
        htmlData = html.unescape(response.decode('utf-8'))
        return BeautifulSoup(htmlData, 'html.parser')

    @staticmethod
    def download_file(url):
        filename = os.path.basename(url)
        urllib.request.urlretrieve(url, filename)
        return filename
