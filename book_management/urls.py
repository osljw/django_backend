from django.urls import path
from.views import BookListCreateView, BookRetrieveUpdateDestroyView, BorrowCreateView, BorrowReturnView

urlpatterns = [
    path('books/', BookListCreateView.as_view()),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view()),
    path('books/<int:book_id>/borrow/', BorrowCreateView.as_view()),
    path('books/<int:book_id>/return/', BorrowReturnView.as_view())
]