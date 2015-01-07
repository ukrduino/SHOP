from django.db import models
import random


class Order(models.Model):
    P1 = "Предопл"
    P2 = "Нал-плат"
    P3 = "Опл-кур"
    P4 = "Опл-маг"
    D1 = "Сам"
    D2 = "НП"
    D3 = "Кур"

    PAY_CHOISES = ((P1, "Предоплата"), (P2, "Наложный платеж"), (P3, "Оплата курьеру"), (P4, "Оплата в магазине"),)
    DELIV_CHOISES = ((D1, "Самовывоз из магазина"), (D2, "Новая Почта"), (D3, "Доставка курьером"),)

    class Meta:
        db_table = 'order'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    order_person = models.CharField(max_length=100, verbose_name='Фамилия Имя Отчество покупателя', blank=False)
    order_person_phone = models.CharField(max_length=30, verbose_name='Контактный телефон', blank=False)
    order_person_address = models.CharField(max_length=200, verbose_name='Адрес доставки', blank=False)
    order_person_email = models.EmailField(verbose_name='E-mail', blank=False)
    order_pay_option = models.CharField(max_length=30, verbose_name='Тип оплаты', blank=False, default=None, choices=PAY_CHOISES)
    order_delivery_option = models.CharField(max_length=30, verbose_name='Тип доставки',
                                             blank=False, choices=DELIV_CHOISES)
    order_date = models.DateTimeField(verbose_name='Дата размещения', auto_now_add=True)
    order_edit_date = models.DateTimeField(verbose_name='Дата редактировани', auto_now=True)
    order_delivered = models.BooleanField(verbose_name='Заказ выполнен', default=False)
    order_confirmed = models.BooleanField(verbose_name='Заказ подтвержден', default=False)
    order_products = models.CharField(max_length=200, verbose_name='Заказанные товары', blank=True)
    order_code = models.CharField(max_length=4, verbose_name='Код заказа', default=random.randint(0, 10000))
    order_password = models.CharField(max_length=15, verbose_name='Пароль к заказу')
    order_sum = models.IntegerField(max_length=5, verbose_name='Сумма заказа', default=0)
    order_discount = models.IntegerField(max_length=4, verbose_name='Скидка заказа', default=0)

# при обращении к классу Order возвращает его код
    def __unicode__(self):
        return self.order_code