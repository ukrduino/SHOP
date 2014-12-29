# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20141229_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffe',
            name='product_сoffe_sort',
            field=models.CharField(max_length=50, choices=[('Робуста', 'Робуста'), ('Арабика', 'Арабика'), ('Робуста+Арабика', 'Робуста + Арабика')], verbose_name='Сорт кофе'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='order_code',
            field=models.CharField(max_length=4, default=6261, verbose_name='Код заказа'),
            preserve_default=True,
        ),
    ]
