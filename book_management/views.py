from rest_framework import generics
from.models import Book, Borrow
from.serializers import BookSerializer, BorrowSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User
from django.http import Http404
import datetime

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BorrowCreateView(generics.CreateAPIView):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer

class BorrowReturnView(generics.UpdateAPIView):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer




class LendMultipleBooksView(APIView):
    def post(self, request):
        book_ids_data = request.data.get('book_ids')
        user_id = request.data.get('user_id')
        print("book_ids:", book_ids_data)
        print("user_id:", user_id)

        if not book_ids_data or not user_id:
            return Response({"message": "Missing book_ids or user_id in the request"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(pk=user_id)
            if not request.user.is_staff:
                return Response({"message": "You are not authorized"}, status=status.HTTP_403_FORBIDDEN)

            book_ids = [int(book_id) for book_id in book_ids_data]
            borrowed_books = []
            for book_id in book_ids:
                try:
                    book = Book.objects.get(pk=book_id)
                    if book.available:
                        book.available = False
                        book.save()
                        borrowed_books.append(Borrow(user=user, book=book, borrow_date=datetime.datetime.now()))
                    else:
                        return Response({"message": f"Book with id {book_id} is not available"}, status=status.HTTP_400_BAD_REQUEST)
                except Book.DoesNotExist:
                    return Response({"message": f"Book with id {book_id} not found"}, status=status.HTTP_404_NOT_FOUND)
            Borrow.objects.bulk_create(borrowed_books)
            return Response({"message": "Books lent successfully"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)