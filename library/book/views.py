from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from authentication.models import CustomUser
from .models import Book
from .forms import BookForm
from order.models import Order
from django.db.models import Q


@login_required
def all_books(request):
    books = Book.objects.all()
    return render(request, "books/all_books.html", {"books": books})


@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "books/book_detail.html", {"book": book})


@login_required
def book_filter(request):
    query = request.GET.get("q", "")
    books = Book.objects.filter(
        Q(name__icontains=query) |
        Q(authors__name__icontains=query) |
        Q(authors__surname__icontains=query) |
        Q(authors__patronymic__icontains=query)
    ).distinct()
    return render(request, "books/book_filter.html", {"books": books, "query": query})


@login_required
def user_books(request, user_id):
    users = CustomUser.objects.all()
    selected_user_id = request.GET.get('user_id')
    orders = []
    selected_user = None

    if selected_user_id:
        selected_user = get_object_or_404(CustomUser, pk=selected_user_id)
        orders = Order.objects.filter(user=selected_user).select_related('book').order_by('-created_at')

    return render(request, "books/user_books.html", {
        "users": users,
        "selected_user": selected_user,
        "orders": orders
    })


@login_required
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_books')
    else:
        form = BookForm()
    return render(request, 'books/create_book.html', {'form': form})


@login_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('all_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/create_book.html', {'form': form, 'edit_mode': True})


@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if not Order.objects.filter(book=book).exists():
        book.delete()
    return redirect('all_books')
