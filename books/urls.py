
__author__ = 'narendra'

from django.conf.urls import include, url
from django.contrib import admin
from books.views import *

urlpatterns = [
    url(r'^$', books_list),
    url(r'^search-form/$', search_form),
    url(r'^search/$', search),
]