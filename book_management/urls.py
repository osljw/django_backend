from django.urls import path
from .views import BookList, AddBook, UpdateBookStatus, BorrowBook, ReturnBook

urlpatterns = [
    path('books/', BookList.as_view(), name='book_list'),
    path('add-book/', AddBook.as_view(), name='add_book'),
    path('update-status/<int:id>/', UpdateBookStatus.as_view(), name='update_status'),
    path('borrow-book/', BorrowBook.as_view(), name='borrow_book'),
    path('return-book/', ReturnBook.as_view(), name='return_book'),
]