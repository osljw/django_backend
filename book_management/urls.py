from django.urls import path
from.views import BookListAPIView, LendMultipleBooksView

urlpatterns = [
    path('books', BookListAPIView.as_view()),
    # path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view()),
    # path('books/<int:book_id>/borrow/', BorrowCreateView.as_view()),
    # path('books/<int:book_id>/return/', BorrowReturnView.as_view())
    path('books/borrow', LendMultipleBooksView.as_view())
]