import logging
from collections import namedtuple
import requests
from urllib.parse import urlparse

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('WB')

class Parser_WB:

    def __init__(self):
        # Create session object and pass request parameters
        self.session = requests.session()
        self.session.headers = {
            '''
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0
             Safari/537.36", 
            "X-Amzn-Trace-Id": "Root=1-62c694ad-599841fa59935a9c18b35f1a"'
            '''
        }
        self.result = []
        self.page_number = str()

    def load_page(self, url):
        try:
            res = self.session.get(url=url)
            res.raise_for_status()
        except ConnectionError:
            res = 1
            print("Connection refused")
        return res.json()

    def parse_json(self, json, query):
        if len(json) == 0:
            print('None')
            return None

        request_name = query
        ParseResult = namedtuple(
            request_name,
            (
                'page_number',
                'article',
                'product_name',
                'brand_name',
            )
        )

        for data in json['data']['products']:
            if data['brand'] == 'ТД Елена':
                logger.info(data)

                self.result.append(ParseResult(
                    self.page_number,
                    data['id'],
                    data['name'],
                    data['brand'],
                ))

    def url_parser(self, url: str):
        num = [num.replace('page=', '') for num in urlparse(url).query.split('&') if 'page=' in num]
        self.page_number = num.pop()

    def run(self, urls: [], query: str):
        for url in urls:
            self.url_parser(url=url)
            logger.info(self.page_number)
            json = self.load_page(
                url=url)
            self.parse_json(json=json, query=query)


