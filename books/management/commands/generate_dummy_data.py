from django.core.management.base import BaseCommand
from authors.models import Author
from publishers.models import Publisher
from books.models import Book, BookTitle
from customers.models import Customer
from django_countries.fields import Country
import random

class Command(BaseCommand):
    help = 'Generate dummy data for testing purpose'

    def handle(self, *args, **kwargs):

        # authors
        authors_list = ['Donald Knuth', 'Alan Turing', 'Edsger W. Dijkstra', 'Andrew S. Tanenbaum']
        for author in authors_list:
            Author.objects.get_or_create(name=author)

        # publishers
        publishers_list = [
            {
            'name': 'Pearson ',
            'country': Country(code='us')
            },
            {
            'name': 'Springer Nature ',
            'country': Country(code='us')
            },
            {
            'name': 'Elsevier',
            'country': Country(code='us')
            }]
        for publisher in publishers_list:
            Publisher.objects.get_or_create(name=publisher['name'], defaults={'country': publisher['country']})

        # books titles
        book_titles_list = ['The Art of Computer Programming', 'Concrete Mathematics: A Foundation for Computer Science', 'On Computable Numbers, with an Application to the Entscheidungsproblem']
        publishers = [pub.name for pub in Publisher.objects.all()]
        items = zip(book_titles_list, publishers)
        for item in items:
            # check if title already exists
            if not BookTitle.objects.filter(title=item[0]).exists():
                # get authors, randomly order and select one
                author = Author.objects.order_by('?').first()
                # get publishers
                publisher = Publisher.objects.get(name=item[1])
                BookTitle.objects.create(title=item[0], publisher=publisher, author=author)

        # books
        book_titles = BookTitle.objects.all()
        for title in book_titles:
            quantity = random.randint(1,5)
            for book in range(quantity):
                Book.objects.get_or_create(title=title)
        
        # customers
        customers_list = [
            {"first_name": "Ayesha", "last_name": "Khan"},
            {"first_name": "Muhammad", "last_name": "Ali"},
            {"first_name": "Fatima", "last_name": "Ahmed"},
            {"first_name": "Imran", "last_name": "Butt"},
            {"first_name": "Zara", "last_name": "Shah"},
            {"first_name": "Usman", "last_name": "Rizvi"},
            {"first_name": "Sana", "last_name": "Malik"},
            {"first_name": "Asif", "last_name": "Mehmood"},
            {"first_name": "Hina", "last_name": "Tariq"},
            {"first_name": "Kamran", "last_name": "Chaudhry"}
        ]
        for customer in customers_list:
            Customer.objects.get_or_create(**customer)