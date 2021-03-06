from django.shortcuts import render_to_response, redirect, render
from store.models import Coffe # импортируем модели
from cart.models import Order # импортируем модели
#from django.core.exceptions import ObjectDoesNotExist  # ошибка - объект не существует
#from django.http.response import Http404  # вывод страницы 404
from cart.forms import OrderForm
from django.core.context_processors import csrf  # защита данных передаваемых из форм
#from django.contrib import auth   # модуль авторизации
from django.template import RequestContext
from django.core.mail import send_mail
from django.contrib import messages

#TODO всю корзину сделать на Ajax


def add_to_cart_main(request, product_id=1):

    if request.session.get('prods_in_cart'):
        prods_in_cart = request.session.get('prods_in_cart')
        prod = Coffe.objects.get(id=product_id)
        prods_in_cart.append(prod.title)
        request.session['prods_in_cart'] = prods_in_cart
        group_prods_in_cart(request, prods_in_cart)
    else:
        prods_in_cart = list()
        prod = Coffe.objects.get(id=product_id)
        prods_in_cart.append(prod.title)
        request.session['prods_in_cart'] = prods_in_cart
        group_prods_in_cart(request, prods_in_cart)

        request.session['cart_qwt_of_prods'] = len(prods_in_cart)

    if request.session.get('cart_cost'):
        add_cart_cost = request.session['cart_cost']
        prod_to_add = Coffe.objects.get(id=product_id)
        add_cart_cost += prod_to_add.product_current_price
        request.session['cart_cost'] = add_cart_cost
    else:
        add_cart_cost = 0
        prod_to_add = Coffe.objects.get(id=product_id)
        add_cart_cost += prod_to_add.product_current_price
        request.session['cart_cost'] = add_cart_cost

    return redirect('home')


def group_prods_in_cart(request, prods_in_cart):
    # группировка товаров... товаров с таким-то id  - 2,
    # с таким-то - 4...  для выписывания счета (создания заказа для сохренения в Б/д)

    prods_in_cart = prods_in_cart
    # создаем словарь для группировки id
    grouped_prods_in_cart = {}
    # для каждого элемента (назовем его prod) в списке prods_in_cart....
    for prod in prods_in_cart:  # http://samag.ru/archive/article/1581
        # если запись с ключем равным такому id(преобразованному в int) уже есть в списке prod_cart_checkout....
        if prod in grouped_prods_in_cart:
            # то увеличиваем ее (записи с ключем равным id товара из списка cart) значение на 1
            grouped_prods_in_cart[prod] += 1
        else:
            # если записи с таким ключем нет то создаем ее...
            grouped_prods_in_cart[prod] = 1
    # и сохраняем отсортированный словарь prod_cart_checkout в session в запись с ключем cart_checkout_items
    request.session['grouped_prods_in_cart'] = grouped_prods_in_cart

    # form = OrderForm
    #
    # return render_to_response('cart.html', {'products': Coffe.objects.all(), 'form': form},
    #                           context_instance=RequestContext(request))


def add_to_cart(request, product_title):
    prods_in_cart = request.session.get('prods_in_cart')
    prods_in_cart.append(product_title)
    request.session['prods_in_cart'] = prods_in_cart
    group_prods_in_cart(request, prods_in_cart)

    request.session['cart_qwt_of_prods'] = len(prods_in_cart)

    add_cart_cost = request.session['cart_cost']
    prod_to_add = Coffe.objects.get(title=product_title)
    add_cart_cost += prod_to_add.product_current_price
    request.session['cart_cost'] = add_cart_cost

    return redirect('home')


def rem_from_cart(request, product_title):
    if product_title in request.session.get('prods_in_cart'):
        rem_usercart = request.session.get('prods_in_cart')
        rem_usercart.remove(product_title)
        request.session['prods_in_cart'] = rem_usercart
        group_prods_in_cart(request, rem_usercart)

        request.session['cart_qwt_of_prods'] = len(rem_usercart)

        rem_cart_cost = request.session.get('cart_cost')
        prod_to_rem = Coffe.objects.get(title=product_title)
        rem_cart_cost -= prod_to_rem.product_current_price
        request.session['cart_cost'] = rem_cart_cost

    return redirect('home')


def cart(request):

    args = dict()

    args['products'] = Coffe.objects.all()
    args['form'] = OrderForm
    request.session['selection_type'] = "Все товары магазина"

    return render_to_response('cart.html', args, context_instance=RequestContext(request))


def make_order(request):

    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            add = form.save(commit=False)
            add.order_products = request.session.get('grouped_prods_in_cart')
            add.order_sum = request.session.get('cart_cost')
            add.save()
            messages.success(request, 'Спасибо за Ваш заказ!\n На Ваш электронный адрес направлено письмо со ссылкой '
                                      'для подтверждения заказа. После подтверждения Вы можете найти свой '
                                      'заказ в разделе заказы по его номеру.')

            shop_email_subject = "Новый заказ !!!"
            shop_email_body = "Поступил новый заказ №%s!\n Покупатель - %s.\n Сумма заказа - %s.\n Товары - %s\n" \
                              % (add.order_code, add.order_person, add.order_sum, add.order_products)
            send_mail(shop_email_subject, shop_email_body, 'Alex.Vlasov.ukr@gmail.com', ['ukrduino@gmail.com'],
                      fail_silently=False)

            conf_link = "127.0.0.1:8000/cart/confirm_order/%s" % add.order_code
            buyer_email_subject = "Ваш заказ в магазине КОФЕ SHOP"
            buyer_email_body = "Добрый день уважаемый %s!!! \n Спасибо за Ваш заказ. Для подтверждения заказа " \
                               "необходимо перейти по ссылке укзанной ниже \n %s" % (add.order_person, conf_link)

            send_mail(buyer_email_subject, buyer_email_body, 'Alex.Vlasov.ukr@gmail.com', ['ukrduino@gmail.com'],
                      fail_silently=False)
        else:
            messages.error(request, 'Ваш заказ НЕ ОФОРМЛЕН!!! Проверьте правильность введения '
                                    'данных и повторите заказ. ВСЕ поля НЕОБХОДИМО заполнить!!!')
    return redirect('cart')



def confirm_order(request, order_code):

    order = Order.objects.get(order_code=order_code)
    order.order_confirmed = True
    order.save()
    shop_email_subject = "Заказ №%s - подтвержден!!!" % order_code
    shop_email_body = "Заказ №%s!\n Покупатель - %s.\n Телефон клиента - %s.\n Товары - %s.\n Сумма заказа - %s.\n " \
                      "Форма оплаты - %s.\n Адрес доставки - %s.\n Способ доставки - %s" \
                      % (order.order_code,
                         order.order_person,
                         order.order_person_phone,
                         order.order_products,
                         order.order_sum,
                         order.order_pay_option,
                         order.order_person_address,
                         order.order_delivery_option)

    send_mail(shop_email_subject, shop_email_body, 'Alex.Vlasov.ukr@gmail.com', ['ukrduino@gmail.com'],
              fail_silently=False)

    return redirect('order_confirmed')
