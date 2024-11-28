from rest_framework import generics
from.models import Book, Borrow
from.serializers import BookSerializer, BorrowSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from user_auth.models import User
from django.http import Http404
import datetime


class BookListAPIView(generics.ListAPIView):
    serializer_class = BookSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = Book.objects.all()
        title = self.request.query_params.get('title', None)
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset



class LendMultipleBooksView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        book_ids_data = request.data.get('bookIds')
        # 从JWT中获取用户信息，进而获取用户ID
        user = request.user
        user_id = user.id
        print("book_ids:", book_ids_data)
        print("user_id:", user_id)

        # if not book_ids_data or not user_id:
        #     return Response({"message": "Missing book_ids or user_id in the request"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(username='admin')
            # user = User.objects.get(pk=user_id)
            # if not request.user.is_staff:
            #     return Response({"message": "You are not authorized"}, status=status.HTTP_403_FORBIDDEN)
            print("user admin:", user)

            book_ids = [int(book_id) for book_id in book_ids_data]
            borrowed_books = []
            for book_id in book_ids:
                try:
                    book = Book.objects.get(id=book_id)
                    if book.borrowed_count >= book.total_count:
                        return Response({'message': '该书籍已无库存，无法借阅'}, status=status.HTTP_400_BAD_REQUEST)
                    book.borrowed_count += 1
                    book.save()
                    borrowed_books.append(Borrow(user=user, book=book, borrow_date=datetime.datetime.now()))
                except Book.DoesNotExist:
                    return Response({"message": f"Book with id {book_id} not found"}, status=status.HTTP_404_NOT_FOUND)
            print("borrowed books:", borrowed_books)
            Borrow.objects.bulk_create(borrowed_books)
            return Response({"message": "Books lent successfully"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)