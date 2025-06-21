from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order
from book.models import Book
from django.utils import timezone


@login_required
def all_orders(request):
    orders = Order.objects.select_related('user', 'book').all()
    return render(request, 'orders/all_orders.html', {'orders': orders})


@login_required
def user_orders(request):
    orders = Order.objects.filter(user=request.user).select_related('book')
    return render(request, 'orders/user_orders.html', {'orders': orders})


@login_required
def create_order(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        try:
            book = Book.objects.get(id=book_id)
            plated_end_at = timezone.now() + timezone.timedelta(days=14)

            order = Order.create(user=request.user, book=book, plated_end_at=plated_end_at)
            if order:
                return redirect('user_orders')
            else:
                error = "Cannot create order — possibly no available copies."
        except Book.DoesNotExist:
            error = "Book does not exist."
    else:
        error = None

    books = Book.objects.all()
    return render(request, 'orders/create_order.html', {'books': books, 'error': error})


@login_required
def close_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if not order.end_at:
        order.end_at = timezone.now()
        order.save()

        book = order.book
        book.count += 1
        book.save()

    return redirect('all_orders')
