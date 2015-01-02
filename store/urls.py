from django.conf.urls import patterns, url
from store.models import Coffe
from django.views.generic import TemplateView, ListView


urlpatterns = patterns('',

                       url(r'^$', ListView.as_view(model=Coffe, template_name="store.html"), name="home"),
                       url(r'^add_product/(?P<product_id>\d+)$', 'cart.views.add_to_cart_main', name='add_main'),)
