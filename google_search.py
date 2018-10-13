import requests
from bs4 import BeautifulSoup, SoupStrainer
import urllib3
from urllib import parse
from lxml import etree
import html2text
import re
import pandas as pd
import relevance

output=open("results.csv","w+")
list=pd.read_csv("Bad_Citation_Searches.csv",delimiter=",", encoding="UTF-8", error_bad_lines=False)
print(list)
for i in range(5):
    search_query = list.loc[i][0]
    url =  "http://www.google.com/search?q=" + parse.quote(search_query)
    url_pool_manager = urllib3.PoolManager()
    response = url_pool_manager.request("GET", url)
    soup = BeautifulSoup(response.data,features='lxml')
    #print(soup)
    soup_ids=soup.find_all("cite")


    #print(soup_ids)

    # SKIP PDF FILES
    for soup_id in soup_ids:
        abc = str(soup_id.decode_contents()).split(".")[-1]
        print(abc)
        if abc != "pdf":
            break

    # print(soup_id)
    soup_id=soup_id.parent
    soup_id = soup_id.parent.parent
    soup_array = soup_id.find('a')['href']
    target_url = soup_array.split('=')[1]
    target_url = target_url.split('&')[0]
    print(target_url)

    # call target url
    response = url_pool_manager.request("GET", target_url)
    bodysoup = BeautifulSoup(response.data,'lxml')

    data = bodysoup.findAll(text=True)

    #print(data)
    def visible(element):
        if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
            return False
        elif re.match('<!--.*-->', str(element.encode('utf-8'))):
            return False
        return True

    result = filter(visible, data)

    # print(result)

    ans = ""
    for element in result:
        ans+=element
    # print(ans)
    match=relevance.token(ans)
    if match>0.25:
        output.write(search_query+","+str(match)+","+target_url+",LEGAL\n")
    else: output.write(search_query+","+str(match)+",N/A,NOT LEGAL\n")
output.close()
    #WORKING CODE FOR ENTIRE TEXT
    # file_object = open(r"sample.txt","w")
    # file_object.write(ans.encode('utf-8'))
