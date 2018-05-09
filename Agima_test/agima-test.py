# -*- coding: utf-8 -*-
import json
import sys

with open('agima/source.json','r') as f:
    json_obj = json.loads(f.read())
    for item in json_obj:
        for k in item.keys():
            sys.stdout.write('<' + k + '>' + item[k] + '</' + k + '>\n')
    