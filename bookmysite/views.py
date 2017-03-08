import datetime

__author__ = 'narendra'

from django.http import HttpResponse, Http404


def home_page_view(request):
    return HttpResponse("welcome to homepage")

def hello(request):
    return HttpResponse("Hello Narendra")

def current_datetime(request):
    now = datetime.datetime.now
    html = "It is now %s." % now
    return HttpResponse(html)

def hours_head(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "In %s hour(s), it will be  %s." % (offset, dt)
    return HttpResponse(html)