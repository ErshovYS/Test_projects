# ~*~ coding: utf-8 ~*~
from django import forms
from test_app.models import OrderModel

class OrderForm(forms.ModelForm):
    phone = forms.CharField(widget = forms.TextInput(attrs={'size':'10'}), 
                               label=u'Номер телефона')
    class Meta:
        model = OrderModel
        fields = ('name', 'some_params')