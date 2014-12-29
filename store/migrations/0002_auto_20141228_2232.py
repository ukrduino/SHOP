# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffe',
            name='product_coffe_type',
            field=models.CharField(max_length=6, verbose_name='Вид кофе', default='РІ Р·РµСЂРЅР°С…', choices=[('молотый', 'молотый'), ('в зернах', 'в зернах')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coffe',
            name='product_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата размещения'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='order_code',
            field=models.CharField(max_length=4, verbose_name='Код заказа', default=9202),
            preserve_default=True,
        ),
    ]
