import datetime
from django.shortcuts import render
from django.template.loader import get_template

__author__ = 'narendra'

from django.http import HttpResponse, Http404
from django.template import Template, Context

# def home_page_view(request):
#     return HttpResponse("welcome to homepage")

def home_page_view(request):
    return render(request, 'homepage.html')


def hello(request):
    return HttpResponse("Hello Narendra")

# def current_datetime(request):
#     now = datetime.datetime.now
#     html = "It is now %s." % now
#     return HttpResponse(html)

# def current_datetime(request):
#     now = datetime.datetime.now
#     html = "<html><body>It is now %s</body></html>" % now
#     return HttpResponse(html)

# def current_datetime(request):
#     now = datetime.datetime.now
#     t = get_template('current_datetime.html')
#     html = t.render(Context({'current_date': now}))
#     return HttpResponse(html)

def current_datetime(request):
    now = datetime.datetime.now
    context = {'current_date': now, 'name':'Narendra Avula'}
    return render(request, 'current_datetime.html', context)


def hours_head(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "In %s hour(s), it will be  %s." % (offset, dt)
    return HttpResponse(html)


def page_one(request):
    return render(request, 'page1.html')

def page_two(request):
    return render(request, 'page2.html')

def page_three(request):
    return render(request, 'page3.html')