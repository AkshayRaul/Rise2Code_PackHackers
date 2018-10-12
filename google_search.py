import requests
from bs4 import BeautifulSoup, SoupStrainer
import urllib3
import urllib
from lxml import etree


search_query = "california"
url =  "http://www.google.com/search?q=" + search_query
url_pool_manager = urllib3.PoolManager()
response = url_pool_manager.request("GET", url)
soup = BeautifulSoup(response.data,features='lxml')
soup_id=soup.find("div",{"id":"search"})
soup_array = soup_id.find('a')['href']
target_url = soup_array.split('=')[1]

# call target url
response = url_pool_manager.request("GET", target_url)

print(response.data)

