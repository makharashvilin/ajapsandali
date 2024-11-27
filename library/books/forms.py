from django import forms
from .models import *

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'author', 'category', 'rating']