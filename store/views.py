from django.shortcuts import render_to_response, redirect, render
from store.models import Coffe, Comment# импортируем модели
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
    args['product'] = Coffe.objects.get(id=product_id)
    args['comments'] = Comment.objects.filter(comment_product_id=product_id)
    args['form'] = comment_form
#    args['username'] = auth.get_user(request).username
# В шаблон lustra_detail.html передаются данные одним словарем args и контекст(с сессией)
    return render_to_response('coffe_detail.html', args, context_instance=RequestContext(request))


def add_comment(request, product_id=1):
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
    return redirect('/coffe/%s' % product_id)

