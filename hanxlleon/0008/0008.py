# -*- coding: utf-8 -*-
import urllib2
import re


baidu_url = 'http://wengengmiao.baijia.baidu.com/article/52893'

class Spider:
    def __init__(self, url=baidu_url):
        self.url = url
        self.user_agent = 'Mozilla/5.0 (Windows NT 5.1; rv:36.0)'
        self.header = { 'User-Agent': self.user_agent  }

    @profile
    def read_page(self):
        try:
            #request = urllib2.Request(self.url, headers=self.header)
            #response = urllib2.urlopen(request)
            response = urllib2.urlopen(self.url)
            page = response.read().decode('utf-8')
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print u'连接出错， 原因：', e.reason
                return None
        return page
    
    @profile
    def article(self, page):
        pattern = re.compile(r'<p class="text">([^<>]*?)</p>', re.S) # 测试了下，这里大概需要5s
        lines = re.findall(pattern, page) # 这里大概需要0.8s
        return ''.join(lines)


if __name__ == '__main__':
    spider = Spider(baidu_url)
    page = spider.read_page()
    print spider.article(page)
