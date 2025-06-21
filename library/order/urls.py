from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.all_orders, name='all_orders'),
    path('user/', views.user_orders, name='user_orders'),
    path('create/', views.create_order, name='create_order'),
    path('close/<int:order_id>/', views.close_order, name='close_order'),
    path('orders/custom/<int:book_id>/', views.custom_order, name='custom_order'),
]
