from django.db import models
from books.models import Book
from django.utils.text import slugify
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(blank=True, unique=True)
    additional_info = models.TextField(blank=True)
    rating = models.PositiveSmallIntegerField(default=50)
    books = models.ManyToManyField(Book, blank=True)
    book_count = models.PositiveSmallIntegerField(help_text="Number of currently rented books by this customer", default=0)

    def __str__(self):
        return str(self.username)
    
    def save(self, *args, **kwargs):
        # if user does not enter a username
        if not self.username:
            # create username
            base_username = f'{self.first_name} {self.last_name}'
            base_slug = slugify(base_username)
            username = base_slug

            suffix = 1
            # check if username already exists or not
            while Customer.objects.filter(username=username).exists():
                username = f'{base_slug}-{suffix}'
                suffix += 1
            # assign new created username 
            self.username = username
        else:
            # if user enters a username, slugify the username
            self.username = slugify(self.username)
        self. book_count = self.books.count()
        super().save(*args, **kwargs)

# update book count when a book is rented or returned
@receiver(m2m_changed, sender=Customer.books.through)
def update_book_count(sender, instance, **kwargs):
    instance.book_count = instance.books.count()
    instance.save(update_fields=['book_count'])

