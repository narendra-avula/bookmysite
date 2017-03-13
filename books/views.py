from django.http import HttpResponse
from django.shortcuts import render
from books.models import Book

# Create your views here.


__author__ = 'narendra'


def search_form(request):
    return render(request, 'books/search_form.html')

# def search(request):
#     if 'query' in request.GET:
#         message = 'You searched for : %r' % request.GET['query']
#     else:
#         message = 'You submitted an empty form'
#     return HttpResponse(message)

def search(request):
    if 'query' in request.GET and request.GET['query']:
        book_name = request.GET['query']
        books = Book.objects.filter(title__icontains=book_name)
        context = {'books': books, 'bookName': book_name}
        return render(request, 'books/search_results.html', context)
    else:
        return HttpResponse('Please submit a search term')