from django.db import models
# импортируем random  для функции make_upload_path
import random
# импортируем модель пользователя
# http://arunrocks.com/building-a-hacker-news-clone-in-django-part-1/
# from django.contrib.auth.models import User
# from django.utils import timezone


# функция Переопределение имени загружаемого файла.  TODO вынести в утилиты
def make_upload_path(instance, filename, prefix=False):
    n1 = random.randint(0, 10000)
    n2 = random.randint(0, 10000)
    n3 = random.randint(0, 10000)
    filename = str(n1)+"_"+str(n2)+"_"+str(n3) + '.jpg'
    return u"%s/%s" % ('static', filename)  # и кладет в папку указ. в "settings" в "IMAGE_UPLOAD_DIR"


class MainClass(models.Model):  # абстрактный класс имеет имя и картинку
    class Meta:
        abstract = True
        app_label = 'Магазин'

    title = models.CharField(max_length=100, verbose_name='Название', blank=False, unique=True)
    slug = models.CharField(max_length=100, verbose_name='URL')
    image = models.ImageField(upload_to=make_upload_path, default="", verbose_name='Изображение')

# при обращении к экземпляру класса возвращает его имя - title ( в админке использует __str__, в др местах __unicode__)
    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

# функция формирования пути к картинке объекта Product для отображения в админке
    def pic(self):  # TODO передавать в функцию высоту файла
        if self.image:  # как заменять адрес сайта ???
            return '<img src="http://127.0.0.1:8000/%s", height="100"/>' % self.image.url
        else:
            return '(none)'
    pic.short_description = 'Изображение'
    pic.allow_tags = True


class Manufacturer(MainClass):  # класс производителя
    class Meta():
        db_table = 'manufect'
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    manufacturer_text = models.TextField(max_length=1000, verbose_name='Описание производителя')
    manufacturer_country = models.CharField(max_length=50, verbose_name='Страна производства', blank=False)


class Product(MainClass):  # абстрактный класс  продукта
    class Meta:
        abstract = True

    product_text = models.TextField(verbose_name='Описание товара', blank=False)
    product_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата размещения', blank=False)
    product_date_change = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    product_likes = models.IntegerField(default=0, verbose_name='Лайки')
    product_sold = models.IntegerField(default=0, verbose_name='Продано штук')
    product_start_price = models.IntegerField(verbose_name='Начальная цена', default=0)
    product_current_price = models.IntegerField(verbose_name='Текущая цена', default=0)
    product_present = models.BooleanField(verbose_name='В наличии', default=True)
    product_order = models.BooleanField(verbose_name='Под заказ', default=False)
    product_manuf = models.ForeignKey(Manufacturer, related_name='coffes')  # производитель товара


class Coffe(Product):  # класс продукта кофе
    P1 = "250 гр"
    P2 = "500 гр"
    P3 = "1 кг"
    P4 = "3 кг"
    T1 = "молотый"
    T2 = "в зернах"
    R1 = "Light"
    R2 = "Light_Medium"
    R3 = "City"
    R4 = "Full_City"
    R5 = "Medium_Dark"
    R6 = "Dark"
    R7 = "French"
    S1 = "Робуста"
    S2 = "Арабика"
    S3 = "Робуста+Арабика"

    P_CHOISES = ((P1, "250 гр"), (P2, "500 гр"), (P3, "1 кг"), (P4, "3 кг"),)
    T_CHOISES = ((T1, "молотый"), (T2, "в зернах"),)
    S_CHOISES = ((S1, "Робуста"), (S2, "Арабика"), (S3, "Робуста + Арабика"), )
    R_CHOISES = ((R1, "Light / светлая"), (R2, "Light / средне-светлая"), (R3, "City / Medium-Light"),
                 (R4, "Full City / Medium"), (R5, "Medium-Dark / Full City+ / венская обжарка"),
                 (R6, "Dark / Italian roast"), (R7, "French roast"),)

    class Meta():
        db_table = 'coffe'  # определяем свое название таблицы в Б.Д.
        verbose_name = 'Кофе'  # имя модели в админке в ед ч
        verbose_name_plural = 'Кофе'  # имя модели в админке в мн ч
    product_сoffe_sort = models.CharField(max_length=50, verbose_name='Сорт кофе', choices=S_CHOISES)
    product_сoffe_roast = models.CharField(max_length=50, verbose_name='Тип обжарки', choices=R_CHOISES)
    product_coffe_wights = models.CharField(max_length=6, verbose_name='Вес упаковки', choices=P_CHOISES)
    product_coffe_type = models.CharField(max_length=8, verbose_name='Вид кофе', choices=T_CHOISES)


class Comment(models.Model):  # TODO добавить пользователя написавшего комментарий
    class Meta():
        db_table = 'comment'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    comment_text = models.TextField(max_length=1000, verbose_name='Текст комментария')
    comment_date = models.DateTimeField(verbose_name='Дата комментария', auto_now=True,)
    comment_product = models.ForeignKey(Coffe)  # связка с моделью Coffe
