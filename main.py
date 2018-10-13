import relevance
import main
import requests
from bs4 import BeautifulSoup, SoupStrainer
import urllib3
import urllib
from lxml import etree
import html2text
import re

result = filter(visible, data)

print list(result)

ans = ""
for element in result:
    ans+=element

#WORKING CODE FOR ENTIRE TEXT
file_object = open(r"sample.txt","w")
file_object.write(ans.encode('utf-8'))