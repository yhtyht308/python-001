# -*- coding: utf-8 -*-
import scrapy
from gitgub.items import GitgubItem

class InfoSpider(scrapy.Spider):
    name = 'info'

    @property
    def start_urls(self):
        url_tmp='https://github.com/shiyanlou?page={}&tab=repositories' 
        return(url_tmp.format(i) for i in range(1,5))

    def parse(self, response):
        for repository in response.css('li.public'):
            yield{
                'name':repository.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first("\n\s*(.*)"),
                'update_time':repository.xpath('.//relative-time/@datetime').extract_first()
                }
