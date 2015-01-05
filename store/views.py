from django.shortcuts import render_to_response, redirect, render
from store.models import *  # импортируем модели
#from django.core.exceptions import ObjectDoesNotExist  # ошибка - объект не существует
#from django.http.response import Http404  # вывод страницы 404
from store.forms import CommentForm
from django.core.context_processors import csrf  # защита данных передаваемых из форм
#from django.contrib import auth   # модуль авторизации
from django.template import RequestContext
from django.contrib import messages


def coffe_detail(request, product_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    product = Coffe.objects.get(id=product_id)
    args['product'] = product
    args['manufacturer'] = product.product_manuf
    args['comments'] = Comment.objects.filter(comment_product_id=product_id)
    args['form'] = comment_form
#    args['username'] = auth.get_user(request).username
# В шаблон lustra_detail.html передаются данные одним словарем args и контекст(с сессией)
    return render_to_response('detail.html', args, context_instance=RequestContext(request))


def home(request):
    args = {}
    # cart_objects = {}
    # if request.session.get('cart_checkout_items'):
    #     cart_checkout_items = request.session.get('cart_checkout_items')
    #     for key, value in cart_checkout_items.items():
    #         item = Coffe.objects.get(id=key)
    #         cart_objects[item.title] = value
    #
    args['manufacturers'] = Manufacturer.objects.all()
    args['products'] = Coffe.objects.all()

    return render_to_response('store.html', args, context_instance=RequestContext(request))


def add_comment(request, product_id=1):
    if 'pause' in request.session:
        messages.error(request, 'Комментарий не опубликован!!! Вы оставили предидущий комментарий менее '
                                '1 минуты назад.')

    if request.POST and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_product = Coffe.objects.get(id=product_id)
            form.save()
            messages.success(request, 'Спасибо за Ваш комментарий!')
            request.session.set_expiry(60)  # создает объект сессии и настраивает срок ее действия -60 секунд
            request.session['pause'] = True  # Внутри сессии создает переменную 'pause' равную TRUE.
        else:
            messages.error(request, 'Сообщение не опубликовано!!!    Вы неправильно ответили '
                                    'на вопрос проверки или оставили сообщение менее '
                                    '1 минуты назад.')
    return redirect('/%s' % product_id)


def manufecturer_filter(request, man_id=1):
    args = dict()

    args['manufacturers'] = Manufacturer.objects.all()
    args['products'] = Coffe.objects.filter(product_manuf_id=man_id)

    return render_to_response('store.html', args, context_instance=RequestContext(request))


def sort_filter(request, sort):
    args = dict()

    args['manufacturers'] = Manufacturer.objects.all()
    args['products'] = Coffe.objects.filter(product_сoffe_sort=sort)
    print(sort)

    return render_to_response('store.html', args, context_instance=RequestContext(request))