__author__ = 'andriy'
from django.conf.urls import patterns, url
from translate import views
urlpatterns = patterns('',
        url(r'^$', views.main, name='main'),
        url(r'^contacts/$', views.contacts, name='contacts'),
        url(r'^search/$', views.search, name='search'),
        url(r'^categories/(?P<category_name_slug>[\w\-]+)/$', views.bands, name='category'),
        url(r'^categories/$', views.categories, name='categories'))