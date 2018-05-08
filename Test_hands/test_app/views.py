# ~*~ coding: utf-8 ~*~
import re

from django.shortcuts import render, render_to_response
from django.template.context import RequestContext

from test_app import forms, models

#Получаем и обрабатываем заказ
def order_form_view(request):
    if request.POST:
        orderform = forms.OrderForm(request.POST)
        if orderform.is_valid():
            params = orderform.cleaned_data
			#Хотел было найти идеальное регулярное выражение для номеров, но нет...
            #phone = re.compile('^(?:\+|\d)[\d\-\(\) ]{4,12}\d$') 
            #phones = phone.findall(params['phone'])
            reg = re.compile('[^\+0-9 ]')
            without_text = reg.sub('', params['phone'])
            phones = []
            for num in without_text.split():
                if len(num) == 7:
                    phones.append('8495' + num)
                elif len(num) == 11 and num[0] == '8':
                    phones.append(num)
                elif len(num) == 12 and num[0] == '+' and num[1] == '7':
                    phones.append(num.replace('+7', '8'))
            #Сохраняем модели
            ordermodel =  models.OrderModel()
            ordermodel.name = params['name']
            ordermodel.some_params = params['some_params']
            ordermodel.save()
            for ph in phones:
                phonemodel = models.PhoneModel()
                phonemodel.phone_number = ph
                phonemodel.save()
                ordermodel.phone_number.add(phonemodel)
        mdict = {'order_form': orderform, 'h2': u'Количество телефонов: ' + str(len(phones))}
    else:
        mdict = {'order_form': forms.OrderForm()}
    return render_to_response("index.html", mdict,
                                              context_instance=RequestContext(request))
    
#По номеру телефона определяем наличие заказов и возвращаем их
def ph_number(request, num):
    phonemodel = models.PhoneModel.objects.filter(phone_number=num).first()
    if phonemodel:
        orders = models.OrderModel.objects.filter(phone_number=phonemodel).only('name')
        mdict = {'orders': orders}
    else:
        mdict = {'h2': u'По заданному номеру заказов нет.'}
    return render_to_response("index.html", mdict,
                                              context_instance=RequestContext(request))