from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_books, name='all_books'),
    path('<int:book_id>/', views.book_detail, name='book_detail'),
    path('user/<int:user_id>/', views.user_books, name='user_books'),
    path('filter/', views.book_filter, name='book_filter'),
    path('create/', views.create_book, name='create_book'),
    path('<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
]
