from rest_framework.response import Response
from rest_framework.views import APIView
from books.models import Book

__author__ = 'narendra'



class Books(APIView):

    def get(self, request):
        books = Book.objects.all()
        return Response({"result": list(books) })