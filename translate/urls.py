__author__ = 'andriy'
from django.conf.urls import patterns, url
from translate import views

urlpatterns = patterns('',
                       url(r'^$', views.main, name='main'),
                       url(r'^contacts/$', views.contacts, name='contacts'),
                       url(r'^categories/(?P<category_id>\d+)/$', views.category, name='category'),
                       url(r'^categories/$', views.categories, name='categories'),
                       url(r'^band/(?P<band_id>\d+)/$', views.band, name='band'),
                       url(r'^translate/(?P<translates_id>\d+)/$', views.translate, name='translate'),)

