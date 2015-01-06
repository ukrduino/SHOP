from django.conf.urls import patterns, url
from store.models import Coffe
from django.views.generic import TemplateView, ListView


urlpatterns = patterns('',
                       url(r'^(?P<product_id>\d+)$', 'store.views.coffe_detail', name='coffe_detail'),
                       # url(r'^filter/(?P<man_id>\d+)$', 'store.views.manufecturer_filter', name='man_filter'),
                       # url(r'^filter/(?P<sort>)', 'store.views.sort_filter', name='sort_filter'),
                       url(r'^add_comment/(?P<product_id>\d+)$', 'store.views.add_comment', name='comment'),
                       # url(r'^$', ListView.as_view(model = Coffe, template_name = "store.html"), name='home'),
                       url(r'^$', 'store.views.home',  name="home"),
                       url(r'^filter2/(?P<sort_id>\d+)$', 'store.views.filter2',  name="filter2"),
                       url(r'^filter/(?P<man_id>\d+)$', 'store.views.filter',  name="filter"),

                       )
