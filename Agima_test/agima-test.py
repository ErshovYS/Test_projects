# -*- coding: utf-8 -*-
import json
import sys

with open('agima/source.json','r') as f:
    json_obj = json.loads(f.read())
    sys.stdout.write('<ul>\n')
    for item in json_obj:
        sys.stdout.write('<li>\n')
        for k in item.keys():
            sys.stdout.write('<' + k + '>' + item[k] + '</' + k + '>\n')
        sys.stdout.write('</li>\n')
    sys.stdout.write('</ul>\n')