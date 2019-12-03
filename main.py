# coding: utf-8

import json
import requests

url = 'https://inamuu.com/wp-json/wp/v2/posts?per_page=10&search=ansible'
headers = {"content-type": "application/json"}
data = requests.get(url, headers=headers)
jsondata = data.json()

for i in jsondata:
    print(json.dumps(i["title"]["rendered"], indent=2,ensure_ascii=False))
    print(json.dumps(i["guid"]["rendered"], indent=2,ensure_ascii=False))

