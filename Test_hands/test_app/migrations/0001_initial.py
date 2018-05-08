# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=500, verbose_name='Имя')),
                ('some_params', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Что-нибудь ещё')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneModel',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('phone_number', models.CharField(max_length=10, verbose_name='Номер телефона')),
            ],
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='phone_number',
            field=models.ManyToManyField(to='test_app.PhoneModel', verbose_name='Номера заказа'),
        ),
    ]
