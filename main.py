# coding: utf-8

import json
import requests
import sys

url = "https://inamuu.com/wp-json/wp/v2/posts?per_page=10&search=ansible
headers = {"content-type": "application/json"}
data = requests.get(url, headers=headers)
jsondata = data.json()

search_list = []
for i in jsondata:
    search_result = { "title" : i["title"]["rendered"], "arg" : i["guid"]["rendered"] }
    search_list.append(search_result)


dict_2 = json.dumps({ "items": search_list }, ensure_ascii=False)
print(dict_2)
