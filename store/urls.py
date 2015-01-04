from django.conf.urls import patterns, url
from store.models import Coffe
from django.views.generic import TemplateView, ListView


urlpatterns = patterns('',

                       url(r'^(?P<product_id>\d+)$', 'store.views.coffe_detail', name='coffe_detail'),
                       url(r'^add_comment/(?P<product_id>\d+)$', 'store.views.add_comment', name='comment'),
                       url(r'^$', 'store.views.home',  name="home"),
                       )
