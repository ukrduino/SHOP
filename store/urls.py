from django.conf.urls import patterns, url
# маленький и клевенький ClassBasedView!!!

from django.views.generic import TemplateView




urlpatterns = patterns('',

    url(r'^$', TemplateView.as_view(template_name="main.html"), name="home"),

)
