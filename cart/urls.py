from django.conf.urls import url, patterns  # покупка товаров

urlpatterns = patterns('',
                       url(r'^/add_product/(?P<product_id>\d+)$', 'cart.views.add_to_cart', name='add'),  # ++
                       url(r'^/rem_product/(?P<product_id>\d+)$', 'cart.views.rem_from_cart', name='rem'),  # --
                       url(r'^/make_order$', 'cart.views.make_order', name='make_order'),  # оформить заказ
                       url(r'^$', 'cart.views.cart', name='my_cart'),)  # переход в карзину с других страниц
