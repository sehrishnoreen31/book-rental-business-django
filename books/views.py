from django.shortcuts import render
from .models import BookTitle, Book


def book_title_list_view(request):
    list_of_book_titles = BookTitle.objects.all()
    context = {
        'list_of_book_titles': list_of_book_titles
    }
    return render(request, 'books/main.html', context)

def book_title_detail_view(request, **kwargs):
    pk = kwargs.get('pk')
    book_detail = BookTitle.objects.get(pk=pk)
    context = {
        'book_detail': book_detail
    }
    return render(request, 'books/detail.html', context)

