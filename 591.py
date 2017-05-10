#!/usr/bin/env python3

import re
import time
import logging

import requests
import bs4


logger = logging.getLogger('591')
log_formatter = logging.Formatter('%(asctime)s|%(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(log_formatter)
logger.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)

url = 'https://rent.591.com.tw/new/?kind=1&region=1&rentprice=0,26000&patternMore=2&option=cold&hasimg=1&not_cover=1&order=posttime&orderType=desc'
link_pattern = re.compile('//rent.591.com.*')
cache = set()

def get_links():
    logger.info('requests 591 ...')
    response = requests.get(url)
    html = bs4.BeautifulSoup(response.text, 'html.parser')
    houses = filter(lambda x: x and x != '\n', html.find(id='content').children)
    houses = map(lambda x: x.find(href=link_pattern), houses)
    houses = map(lambda x: 'https:' + x.get('href').strip(), houses)
    return tuple(houses)

while True:
    houses = get_links()
    for h in houses:
        if h in cache:
            break
        logger.info('new house: {}'.format(h))
    cache.update(houses)
    time.sleep(10)