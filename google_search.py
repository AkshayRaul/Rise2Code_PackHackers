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
    url = "http://www.google.com/search?q=" + parse.quote(search_query)
    url_pool_manager = urllib3.PoolManager()
    search_response = url_pool_manager.request("GET", url)
    search_response_DOM = BeautifulSoup(search_response.data,features='lxml')
    #print(soup)
    cite_ids=search_response_DOM.find_all("cite")


    #print(soup_ids)

    # Skip PDF files and select first non-pdf file in results page.
    for cite_id in cite_ids:
        last_segment = str(cite_id.decode_contents()).split(".")[-1]
        #print(segment)
        if last_segment != "pdf":
            break

    # print(soup_id)
    # get the anchor
    if cite_id is None:
        output.write(search_query + "," + str(match) + ",N/A,NOT LEGAL\n")
        continue

    anchor_element_cite_id=cite_id.parent.parent.parent
    if anchor_element_cite_id is None:
        output.write(search_query + "," + str(match) + ",N/A,NOT LEGAL\n")
        continue

    anchor_url = anchor_element_cite_id.find('a')['href']
    target_url = anchor_url.split('=')[1]
    target_url = target_url.split('&')[0]
    print(target_url)

    # call target url
    try:
        response = url_pool_manager.request("GET", target_url)
    except requests.exceptions.ConnectionError:
        output.write(search_query + "," + str(match) + ",N/A,NOT LEGAL\n")
        continue

    if response.status != 200:
        output.write(search_query + "," + str(match) + ",N/A,NOT LEGAL\n")
        continue

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
