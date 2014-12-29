# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import store.models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coffe',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('product_title', models.CharField(verbose_name='Название товара', max_length=100, unique=True)),
                ('product_slug', models.CharField(verbose_name='URL', max_length=100)),
                ('product_text', models.TextField(verbose_name='Описание товара')),
                ('product_date', models.DateTimeField(verbose_name='Дата размещения')),
                ('product_date_change', models.DateTimeField(verbose_name='Дата изменения', auto_now=True)),
                ('product_likes', models.IntegerField(verbose_name='Лайки', default=0)),
                ('product_image', models.ImageField(upload_to=store.models.make_upload_path, verbose_name='Изображение', default='')),
                ('product_sold', models.IntegerField(verbose_name='Продано штук', default=0)),
                ('product_start_price', models.IntegerField(verbose_name='Начальная цена', default=0)),
                ('product_current_price', models.IntegerField(verbose_name='Текущая цена', default=0)),
                ('product_present', models.BooleanField(verbose_name='В наличии', default=True)),
                ('product_order', models.BooleanField(verbose_name='Под заказ', default=False)),
                ('product_prod', models.CharField(verbose_name='Производитель', max_length=50)),
                ('product_country', models.CharField(verbose_name='Страна', max_length=50)),
                ('product_сoffe_type', models.CharField(verbose_name='Сорт кофе', max_length=50)),
                ('product_сoffe_obzh', models.CharField(verbose_name='Тип обжарки', max_length=50)),
                ('product_coffe_wights', models.CharField(verbose_name='Вес упаковки', max_length=6, choices=[('250 гр', '250 гр'), ('500 гр', '500 гр'), ('1 кг', '1 кг'), ('3 кг', '3 кг')])),
            ],
            options={
                'db_table': 'coffe',
                'verbose_name': 'Кофе',
                'verbose_name_plural': 'Кофе',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('comment_text', models.TextField(verbose_name='Текст комментария', max_length=1000)),
                ('comment_date', models.DateTimeField(verbose_name='Дата комментария', auto_now=True)),
                ('comment_product', models.ForeignKey(to='store.Coffe')),
            ],
            options={
                'db_table': 'comment',
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('order_person', models.CharField(verbose_name='Фамилия Имя Отчество покупателя', max_length=100)),
                ('order_person_phone', models.CharField(verbose_name='Контактный телефон', max_length=30)),
                ('order_person_address', models.CharField(verbose_name='Адрес доставки', max_length=100)),
                ('order_person_email', models.EmailField(verbose_name='E-mail', max_length=100)),
                ('order_pay_option', models.CharField(verbose_name='Тип оплаты', max_length=30, choices=[('Пр-опл', 'Предоплата'), ('Нал-плат', 'Наложный платеж'), ('Опл-кур', 'Оплата курьеру'), ('Опл-маг', 'Оплата в магазине')])),
                ('order_delivery_option', models.CharField(verbose_name='Тип доставки', max_length=30, choices=[('Сам', 'Самовывоз из магазина'), ('НП', 'Новая Почта'), ('Кур', 'Доставка курьером')])),
                ('order_date', models.DateTimeField(verbose_name='Дата размещения', default=django.utils.timezone.now)),
                ('order_delivered', models.BooleanField(verbose_name='Заказ выполнен', default=False)),
                ('order_confirmed', models.BooleanField(verbose_name='Заказ подтвержден', default=False)),
                ('order_products', models.CharField(verbose_name='Заказанные товары', max_length=200, blank=True)),
                ('order_code', models.CharField(verbose_name='Код заказа', max_length=4, default=6835)),
                ('order_password', models.CharField(verbose_name='Пароль к заказу', max_length=15)),
                ('order_summ', models.IntegerField(verbose_name='Сумма заказа', max_length=4, default=0)),
            ],
            options={
                'db_table': 'order',
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
            bases=(models.Model,),
        ),
    ]
