# -*- coding: utf-8 -*-
import html
import json
import sys

#Парсим тег на классы и идентификаторы
def parse_key(key):
    k1 = key.split('#')
    ids = 'id="'
    if len(k1) > 1:
        for i in range(1, len(k1)):
            ids = '{0} {1}'.format(ids, k1[i])
        ids = '{0} {1}'.format(ids, '"')
    k1 = k1[0].split('.')
    classes = 'class="'
    if len(k1) > 1:
        for i in range(1, len(k1)):
            classes = '{0} {1}'.format(classes, k1[i])
        classes = '{0}{1}'.format(classes, '"') 
    return ['<{0} {1} {2}>'.format(k1[0], ids, classes), '</{0}>'.format(k1[0])]

#Рекурсивная функция создания списков
def rec_func(json_obj):
    sys.stdout.write('<ul>\n')
    for item in json_obj:
        sys.stdout.write('<li>\n')
        for k in item.keys():
            k_parsed = parse_key
            if type(item[k]) == list:
                sys.stdout.write(k_parsed[0])
                rec_func(item[k])
                sys.stdout.write(k_parsed[1])
            else:
                sys.stdout.write('{0}{1}{2}\n'.format(k_parsed[0], html.escape(item[k]), k_parsed[1]))
        sys.stdout.write('</li>\n')
    sys.stdout.write('</ul>\n')


with open('agima/source.json','r') as f:
    json_obj = json.loads(f.read())
    if type(json_obj) == list:
        rec_func(json_obj)
    else:
        for k in json_obj.keys():
            k_parsed = parse_key(k)
            #Только заметил эту дырку (которой нет в примерах) в 4 задаче
            if type(json_obj[k]) == list:
                sys.stdout.write(k_parsed[0])
                rec_func(json_obj[k])
                sys.stdout.write(k_parsed[1])
            else:
                sys.stdout.write('{0}{1}{2}\n'.format(k_parsed[0], html.escape(json_obj[k]), k_parsed[1]))