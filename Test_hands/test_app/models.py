# ~*~ coding: utf-8 ~*~
from django.db import models
    
class PhoneModel(models.Model): 
    phone_number = models.CharField(max_length=10, verbose_name=u'Номер телефона')
    
    def __str__(self):
        return self.phone_number

class OrderModel(models.Model):
    name = models.CharField(max_length=500, verbose_name=u'Имя')
    some_params = models.CharField(max_length=1000, blank=True, null=True, verbose_name=u'Что-нибудь ещё')
    phone_number = models.ManyToManyField(PhoneModel, verbose_name=u'Номера заказа')
    
    def __str__(self):
        return self.name