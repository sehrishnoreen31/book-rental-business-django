from django.shortcuts import render
from books.models import Book
from rentals.models import Rental
from customers.models import Customer
from authors.models import Author
from publishers.models import Pubisher

# home page
def home_view(request):
    books_list = Book.objects.all()
    rentals_list = Rental.objects.all()
    customers_list = Customer.objects.all()
    authors_list = Author.objects.all()
    publishers_list = Pubisher.objects.all()
    context = {
        'books_list': books_list,
        'rentals_list': rentals_list,
        'customers_list': customers_list,
        'authors_list': authors_list,
        'publishers_list': publishers_list,

    }
    return render(request, 'main.html', context=context)