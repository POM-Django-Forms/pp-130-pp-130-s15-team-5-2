from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('users/', views.all_users, name='all_users'),
    path('users/<int:user_id>/', views.user_details, name='user_details'),
]
