# -*- coding: utf-8 -*-
import urllib
import requests
from bs4 import BeautifulSoup
import os

url = 'http://tieba.baidu.com/p/2166231880'
r = requests.get(url)
soup = BeautifulSoup(r.content)

imgurls = [imglink.get('src') for imglink in soup.find_all('img') 
        if imglink.get('pic_type') == '0']

for imgurl in imgurls:
     urllib.urlretrieve(imgurl, os.path.split(imgurl)[1])
