# coding: utf-8

import json
import os
import requests

path = str(os.environ['HOME']) + '/.alfred.workflow.wps.siteurl'

if os.path.isfile(path) is True:
    filepath = open(path, 'r')
    for row in filepath:
        siteurl = row.strip()

url = siteurl + "/wp-json/wp/v2/posts?per_page=10&search={query}"
headers = {"content-type": "application/json"}
data = requests.get(url, headers=headers)
jsondata = data.json()

search_list = []
for i in jsondata:
    search_result = { "title" : i["title"]["rendered"], "arg" : i["guid"]["rendered"] }
    search_list.append(search_result)

postsdata = json.dumps({ "items": search_list }, ensure_ascii=False)
print(postsdata)

