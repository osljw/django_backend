from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from user_auth.models import User

class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        return Response({'books': [{'id': b.id, 'title': b.title, 'author': b.author, 'isbn': b.isbn, 'status': b.status} for b in books]})

class AddBook(APIView):
    def post(self, request):
        data = request.data
        Book.objects.create(
            title=data['title'],
            author=data['author'],
            isbn=data['isbn']
        )
        return Response(status=status.HTTP_201_CREATED)

class UpdateBookStatus(APIView):
    def put(self, request):
        data = request.data
        book = Book.objects.get(id=data['id'])
        book.status = data['new_status']
        book.save()
        return Response(status=status.HTTP_200_OK)

class BorrowBook(APIView):
    def post(self, request):
        data = request.data
        book = Book.objects.get(isbn=data['isbn'])
        book.status = 'borrowed'
        book.save()
        return Response(status=status.HTTP_200_OK)

class ReturnBook(APIView):
    def post(self, request):
        data = request.data
        book = Book.objects.get(isbn=data['isbn'])
        book.status = 'available'
        book.save()
        return Response(status=status.HTTP_200_OK)