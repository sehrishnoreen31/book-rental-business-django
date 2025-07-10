from django.shortcuts import render
from books.models import Book, BookTitle
from rentals.models import Rental
from customers.models import Customer
from authors.models import Author
from publishers.models import Publisher

# home page
def home_view(request):
    books_list = Book.objects.all()
    rentals_list = Rental.objects.all()
    customers_list = Customer.objects.all()
    authors_list = Author.objects.all()
    publishers_list = Publisher.objects.all()

    # reverse relationships
    obj = BookTitle.objects.get(id=11)
    books = obj.books

    context = {
        'books_list': books_list,
        'rentals_list': rentals_list,
        'customers_list': customers_list,
        'authors_list': authors_list,
        'publishers_list': publishers_list,
        'reverse_book_booktitle': books

    }
    return render(request, 'main.html', context=context)