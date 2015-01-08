from django.conf.urls import url, patterns  # покупка товаров
from django.views.generic import TemplateView

urlpatterns = patterns('cart.views',

                       # добавление товара в корзину
                       url(r'add_product/(?P<product_id>\d+)$', 'add_to_cart_main', name='add_main'),
                       url(r'cart_add_product/(?P<product_title>\w+)$', 'add_to_cart', name='add'),  # ++
                       url(r'cart_rem_product/(?P<product_title>\w+)$', 'rem_from_cart', name='rem'),  # --
                       url(r'make_order$', 'make_order', name='make_order'),  # оформить заказ
                       url(r'confirm_order/(?P<order_code>\d+)$', 'confirm_order', name='confirm_order'),  # подтвердить заказ
                       url(r'order_confirmed/$', TemplateView.as_view(template_name='order_confirmed.html'),
                           name="order_confirmed"),  #  заказ подтвержден
                       url(r'$', 'cart', name='my_cart'),  # переход в карзину с других страниц
                       )
