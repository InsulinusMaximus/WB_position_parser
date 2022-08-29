# coding: utf-8
import csv
import logging
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('Repository')

HEADERS = (
    'page_number',
    'article',
    'product_name',
    'brand_name',
    'request_name',
)


class Repository:

    def __init__(self, result):
        self.result = result

    def save_genera_data(self):
        path = f'C:/Users/Pavel/PycharmProjects/WB_position_parser/WB_position_{datetime.now().strftime("%Y%m%d-%H%M%S")}.csv'
        with open(path, 'w', encoding="utf-8", newline="") as f:
            writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL, delimiter=';')
            writer.writerow(HEADERS)
            for item in self.result:
                writer.writerow(item)

    def run(self):
        self.save_genera_data()
