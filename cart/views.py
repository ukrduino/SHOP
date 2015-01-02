from django.shortcuts import render_to_response, redirect, render
from store.models import Coffe # импортируем модели
#from django.core.exceptions import ObjectDoesNotExist  # ошибка - объект не существует
#from django.http.response import Http404  # вывод страницы 404
from cart.forms import OrderForm
from django.core.context_processors import csrf  # защита данных передаваемых из форм
#from django.contrib import auth   # модуль авторизации
from django.template import RequestContext
from django.core.mail import send_mail
from django.contrib import messages


def add_to_cart_main(request, product_id=1):
    if request.session.get('cart'):
        add_usercart = request.session.get('cart')
        add_usercart.append(product_id)
        request.session['cart'] = add_usercart
    else:
        add_usercart = list()
        add_usercart.append(product_id)
        request.session['cart'] = add_usercart

    if request.session.get('cart_prods'):
        add_cart_prods = request.session['cart_prods']
        add_cart_prods += 1
        request.session['cart_prods'] = add_cart_prods
    else:
        add_cart_prods = 0
        add_cart_prods += 1
        request.session['cart_prods'] = add_cart_prods

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
    return redirect('lustra_list')


def cart(request):  # группировка товаров... товаров с таким-то id  - 2,
                    # с таким-то - 4...  для выписывания счета (создания заказа для сохренения в Б/д)
    # из словаря session получаем запись соотв ключу cart - в ней список с id выбранных товаров
    cart_checkout = request.session.get('cart')
    # создаем словарь для группировки id
    prod_cart_checkout = {}
    # для каждого элемента (назовем его prod) в списке cart_checkout....
    for prod in cart_checkout:  # http://samag.ru/archive/article/1581
        # если запись с ключем равным такому id(преобразованному в int) уже есть в списке prod_cart_checkout....
        if int(prod) in prod_cart_checkout:
            # то увеличиваем ее (записи с ключем равным id товара из списка cart) значение на 1
            prod_cart_checkout[int(prod)] += 1
        else: # если записи с таким ключем нет то создаем ее...
            prod_cart_checkout[int(prod)] = 1
    # и сохраняем отсортированный словарь prod_cart_checkout в session в запись с ключем prods
    request.session['prods'] = prod_cart_checkout
    form = OrderForm

    return render_to_response('cart.html', {'products': Coffe.objects.all(), 'form': form},
                              context_instance=RequestContext(request))


def add_to_cart(request, product_id=1):
    add_usercart = request.session.get('cart')
    add_usercart.append(product_id)
    request.session['cart'] = add_usercart
    add_cart_prods = request.session['cart_prods']
    add_cart_prods += 1
    request.session['cart_prods'] = add_cart_prods
    add_cart_cost = request.session['cart_cost']
    prod_to_add = Coffe.objects.get(id=product_id)
    add_cart_cost += prod_to_add.product_current_price
    request.session['cart_cost'] = add_cart_cost
    return redirect(cart)


def rem_from_cart(request, product_id=1):
    if product_id in request.session.get('cart'):
        if request.session.get('cart'):
            rem_usercart = request.session.get('cart')
            rem_usercart.remove(product_id)
            request.session['cart'] = rem_usercart
        if request.session.get('cart_prods') > 0:
            rem_cart_prods = request.session.get('cart_prods')
            rem_cart_prods -= 1
            request.session['cart_prods'] = rem_cart_prods
        if request.session.get('cart_cost') > 0:
            rem_cart_cost = request.session.get('cart_cost')
            prod_to_rem = Coffe.objects.get(id=product_id)
            rem_cart_cost -= prod_to_rem.product_current_price
            request.session['cart_cost'] = rem_cart_cost

    return redirect(cart)


def make_order(request):

    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            add = form.save(commit=False)
            add.order_products = request.session.get('cart')
            add.order_sum = request.session.get('cart_cost')
            add.save()
            messages.success(request, 'Спасибо за Ваш заказ, на Ваш электронный адрес'
                                      'направлено письмо со ссылкой для подтверждения заказа. '
                                      'После подтверждения Вы можете найти/изменить свой заказ '
                                      'в разделе заказы по его номеру.')
            send_mail("АЛЕ!!!!", "У вас новый заказ!!!", 'Alex.Vlasov.ukr@gmail.com', ['ukrduino@gmail.com'], fail_silently=False)
        else:
            messages.error(request, 'Ваш заказ НЕ ОФОРМЛЕН!!! Проверьте правильность введения '
                                    'данных и повторите заказ. ВСЕ поля НЕОБХОДИМО заполнить!!!')
    return redirect(cart)