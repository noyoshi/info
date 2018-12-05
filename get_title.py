#!/usr/bin/env python3
import urllib
from bs4 import BeautifulSoup
import sys

url = sys.argv[1]
try:
    soup = BeautifulSoup(urllib.request.urlopen(url), "lxml")
    print(soup.title.string)
except:
    print(url)
