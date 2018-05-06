# -*- coding: utf-8 -*-
import json
import sys

with open('agima/source.json','r') as f:
    tag_dict = {'title': 'h1', 'body': 'p'}
    json_text = f.read()
    json_obj = json.loads(json_text)
    for item in json_obj:
        for k in item.keys():
            sys.stdout.write('<' + tag_dict[k] + '>' + item[k] + '</' + tag_dict[k] + '>\n')
    