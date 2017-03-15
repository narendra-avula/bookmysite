from django.conf.urls import patterns, url
from books.api_views import *

__author__ = 'narendra'

urlpatterns = [
    'books.api_views',
    url(r'books$', Books.as_view()),
]