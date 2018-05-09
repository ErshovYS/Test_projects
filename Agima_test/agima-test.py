# -*- coding: utf-8 -*-
import json
import sys

#Если внутри списка найден список, то функция вызывается рекурсивно с найденным списком
def rec_func(json_obj):
    sys.stdout.write('<ul>\n')
    for item in json_obj:
        sys.stdout.write('<li>\n')
        for k in item.keys():
            if type(item[k]) == list:
                sys.stdout.write('<' + k + '>\n')
                rec_func(item[k])
                sys.stdout.write('</' + k + '>\n')
            else:
                sys.stdout.write('<' + k + '>' + item[k] + '</' + k + '>\n')
        sys.stdout.write('</li>\n')
    sys.stdout.write('</ul>\n')

with open('agima/source.json','r') as f:
    json_obj = json.loads(f.read())
    rec_func(json_obj)
    