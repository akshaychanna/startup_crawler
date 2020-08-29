import requests
from bs4 import BeautifulSoup
import json
import pprint
import pdb
import re
#from elasticseach import Elasticsearch
#from elasticseach import helpers

#  Connection to database
# es  = Elasticsearch(['http://localhost:9200/'], verify_certs=True)
# url = "https://www.fundoodata.com/citiesindustry/19/7/list-of-information-technology-(it)-companies-in-pune?&pageno=1&tot_rows=740&total_results=740&no_of_offices=0"
url = "https://www.fundoodata.com/citiesindustry/19/7/list-of-information-technology-(it)-companies-in-pune"
data = requests.get(url)
soup = BeautifulSoup(data.content, 'html.parser')
all_divs = soup.find_all("div", class_="search-result")
data_arr = []

for i in all_divs:

    obj = {}
    tag = i.find("div", class_ = "heading")
    if tag != None:
        obj['CompanyName'] = tag.get_text()
        obj['location'] =  (re.sub('\t','',re.sub('\n','',i.find("div", class_="normal-detail").find("td" , text="Location").find_next_siblings()[0].get_text()))).strip(": ")
        obj['website link'] = i.find("div", class_="normal-detail").find("td" , text="Website").find_next_siblings()[0].find("a").get("href")
        #pdb.set_trace()
        #
        data = requests.get(obj["website link"])
        web_soup = BeautifulSoup(data.content, 'html.parser')
        aa = web_soup.find_all("a")
        pattern = "Contact Us"
        hh = list(filter(lambda x: x.get_text()== pattern ,aa))
        print(hh)
        if hh != None:
        	obj["contact us URL"] = hh[0].get('href')
        else:
        	bb = web_soup.find_all("li")
        	jj = list(filter(lambda x: x.get_text()==pattern ,bb))
        	if jj != None:
        		obj["contact us URL"] = jj[0].get('href')
        data_arr.append(obj)


pdb.set_trace()
