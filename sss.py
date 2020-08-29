import requests
from bs4 import BeautifulSoup
import json
import pprint
import pdb
import re


# url = "https://blog.linkedin.com/2019/september/4/-the-2019-linkedin-top-startups-are-growing-fast-and-hiring-even-faster"
url = "https://about.crunchbase.com/blog/50-hottest-tech-companies-2019/"
data_arr = []
data = requests.get(url)
soup = BeautifulSoup( data.content , 'html.parser')
# lis = soup.find("ol").find_all("li")
# for i in lis:
# 	obj = {}
# 	obj["company name"] = i.get_text()
# 	obj["website link"] = i.p.a.get('href')
# 	data_arr.append(obj)
# 	# pdb.set_trace()
# 	print(obj["website link"])
# 	web_data = requests.get(obj["website link"])
# 	web_soup = BeautifulSoup(web_data.content , 'html.parser')

pdb.set_trace()