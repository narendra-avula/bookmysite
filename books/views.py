from django.http import HttpResponse
from django.shortcuts import render
from books.models import Book

# Create your views here.


__author__ = 'narendra'

def books_list(request):
    books = Book.objects.all()
    context  =  {'books': books}
    return render(request, 'books/booksList.html', context)

def search_form(request):
    return render(request, 'books/search_form.html')

# def search(request):
#     if request.method == 'GET':
#         q = request.GET['q']
#         if q:
#             message = 'You searched for : %r' % request.GET['q']
#         else:
#             message = 'You submitted an empty form'
#         return HttpResponse(message)


def search(request):
    if 'query' in request.GET and request.GET['query']:
        book_name = request.GET['query']
        books = Book.objects.filter(title__icontains=book_name)
        context = {'books': books, 'bookName': book_name}
        return render(request, 'books/search_results.html', context)
    else:
        return HttpResponse('Please submit a search term')