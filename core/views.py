from django.shortcuts import render
from books.models import Book

# home page
def home_view(request):
    books_list = Book.objects.all()
    context = {
        'books_list': books_list
    }
    return render(request, 'main.html', context=context)