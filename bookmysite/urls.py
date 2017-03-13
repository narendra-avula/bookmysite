"""bookmysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
Myurls
    url(r'^datetime/plus/(?P<offset>(\d{1,2}))/(?P<value>(\d{1,2}))/$', hours_head)

"""
from django.conf.urls import include, url
from django.contrib import admin
from bookmysite.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls) ),
    url(r'^$', home_page_view ),
    url(r'^mobile/$', home_page_mobile_view ),
    url(r'^hello/$', hello ),
    url(r'^datetime/$', current_datetime ),
    url(r'^datetime/plus/(?P<offset>(\d{1,2}))/$', hours_head),
    url(r'^page1/$', page_one),
    url(r'^page2/$', page_two),
    url(r'^page3/$', page_three),
    url(r'^meta-data/$', display_meta),
    url(r'^books/', include('books.urls'))
]
