import pdb
import sys
from scripts.adpter import Adpter
import pprint
import logging


if __name__ == '__main__':
    print("scrapping started")
    url = "https://www.fundoodata.com/citiesindustry/19/7/list-of-information-technology-(it)-companies-in-pune"
    adpter = Adpter(url)
    list_of_data = adpter.process_target()
    
    print("adding scraped data into NoSql ElasticSearch database:")
    pprint.pprint(list_of_data)
    # adpter.add_to_es(list_of_data)
    
