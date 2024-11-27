from django.shortcuts import render, redirect, get_object_or_404
# from .models import Category, Author, Book
from .forms import *

def home_books(request):
    books = Book.objects.filter(rating__gt=6)
    return render(request, 'home_books.html', {'books': books})


def create_book(request):
    form = BookForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home_books')
    return render(request, 'create_book.html', {'form': form})


def update_book(request, id):
    book = get_object_or_404(Book, id=id)
    form = BookForm(request.POST, instance=book)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home_books')
    return render(request, 'update_book.html', {'form': form, 'book': book})


def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('home_books')
    return render(request, 'delete_book.html', {'book': book})


def detail_book(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'detail_book.html', {'book': book})