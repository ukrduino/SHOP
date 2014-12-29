# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20141228_2232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffe',
            name='product_сoffe_obzh',
        ),
        migrations.AddField(
            model_name='coffe',
            name='product_сoffe_roast',
            field=models.CharField(default='Light / СЃРІРµС‚Р»Р°СЏ', verbose_name='Тип обжарки', choices=[('Light', 'Light / светлая'), ('Light/Medium', 'Light / средне-светлая'), ('City', 'City / Medium-Light'), ('Full City', 'Full City / Medium'), ('Medium-Dark', 'Medium-Dark / Full City+ / венская обжарка'), ('Dark', 'Dark / Italian roast'), ('French', 'French roast')], max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coffe',
            name='product_coffe_type',
            field=models.CharField(verbose_name='Вид кофе', choices=[('молотый', 'молотый'), ('в зернах', 'в зернах')], max_length=8),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='order_code',
            field=models.CharField(default=3599, verbose_name='Код заказа', max_length=4),
            preserve_default=True,
        ),
    ]
