from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.home_books, name='home_books'),
    path('create_book/', views.create_book, name='create_book'),
    path('update_book/<int:id>/', views.update_book, name='update_book'),
    path('delete_book/<int:id>/', views.delete_book, name='delete_book'),
    path('detail_book/<int:id>/', views.detail_book, name='detail_book'),
]