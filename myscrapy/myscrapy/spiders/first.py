import re
import scrapy
from  bs4 import BeautifulSoup
from myscrapy.items import MyscrapyItem
from scrapy.http import Request


class first(scrapy.Spider):
    name = 'first'

    def start_requests(self):
        url = 'https://cuiqingcai.com/3472.html'
        yield Request(url, self.parse)

    def parse(self, response):
        bs = BeautifulSoup(response.text, 'html.parser')
        art = bs.find('article')
        print art.text
