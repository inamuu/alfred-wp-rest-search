# coding: utf-8

import json
import requests

url = 'https://inamuu.com/wp-json/wp/v2/posts?per_page=1&search=ansible'
headers = {"content-type": "application/json"}
data = requests.get(url, headers=headers)
jsondata = data.json()
print(json.dumps(jsondata[0]["title"]["rendered"], indent=2,ensure_ascii=False))

