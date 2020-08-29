from bs4 import BeautifulSoup
import requests
import pdb
import json
# from elasticsearch import Elasticsearch
# from elasticsearch import helpers
import logging
import pprint
import re


class Adpter(object):
    def __init__(self,url):
        self.url = url
        # self.es  = Elasticsearch(['http://localhost:9200/'], verify_certs=True)

    def process_target(self):
        data = requests.get(self.url)
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
                #hh = list(filter(lambda x: x.get_text()== pattern ,aa))
                print(hh)
                if hh != None:
                    obj["contact us URL"] = hh[0].get('href')
                else:
                    bb = web_soup.find_all("li")
                    jj = list(filter(lambda x: x.get_text()==pattern ,bb))
                    if jj != None:
                        obj["contact us URL"] = jj[0].get('href')
                data_arr.append(obj)
        return data_arr
    
    # def add_data_to_es(self,bulk_data):
    #     resp = helpers.bulk(
    #         self.es,
    #         bulk_data,
    #         index = "startup_data",
    #         doc_type = "_doc"
    #     )

