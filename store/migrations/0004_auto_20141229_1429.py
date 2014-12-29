# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20141229_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffe',
            name='product_сoffe_type',
        ),
        migrations.AddField(
            model_name='coffe',
            name='product_сoffe_sort',
            field=models.CharField(default='РђСЂР°Р±РёРєР°', choices=[('Робуста', 'Робуста'), ('Арабика', 'Арабика')], verbose_name='Сорт кофе', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='order_code',
            field=models.CharField(default=4463, verbose_name='Код заказа', max_length=4),
            preserve_default=True,
        ),
    ]
