# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


class Spider:
    def __init__(self, url):
        self.url = url

    def get_page(self):
        r = requests.get(self.url)
        page =  r.content
        return page

    def links(self, page):
        soup = BeautifulSoup(page)
        links = [link.get('href') for link in soup.find_all('a') 
                if link.get('href') and link.get('href').startswith('http')]
        return '\n'.join(links)


if __name__ == '__main__':
    baidu_url = 'http://wengengmiao.baijia.baidu.com/article/52893'
    spider = Spider(baidu_url)
    page = spider.get_page()
    links = spider.links(page)
    print links
    

