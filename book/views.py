import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book, User, Borrowing
from .serializers import BookSerializer, UserSerializer, BorrowingSerializer

class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

class AddBook(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class AddUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BorrowBook(APIView):
    def post(self, request):
        data = request.data
        book_id = data.get('book')
        user_id = data.get('user')
        
        try:
            book = Book.objects.get(id=book_id)
            user = User.objects.get(id=user_id)
            
            borrowing = Borrowing(book=book, user=user)
            borrowing.save()
            return Response({"message": "Book borrowed successfully"}, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

class ReturnBook(APIView):
    def post(self, request):
        data = request.data
        borrowing_id = data.get('borrowing')
        
        try:
            borrowing = Borrowing.objects.get(id=borrowing_id)
            borrowing.return_date = datetime.now()
            borrowing.save()
            return Response({"message": "Book returned successfully"}, status=status.HTTP_200_OK)
        except Borrowing.DoesNotExist:
            return Response({"error": "Borrowing not found"}, status=status.HTTP_404_NOT_FOUND)