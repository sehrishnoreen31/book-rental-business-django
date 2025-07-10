from django.db import models
from books.models import Book
from customers.models import Customer
from datetime import timedelta
from .choices import STATUS_CHOICES

class Rental(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    rent_start_date = models.DateField(help_text='Date when book was rented')
    rent_end_date = models.DateField(help_text='Deadline to return', blank=True)
    return_date = models.DateField(help_text='When book was actually returned', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.book.title} rented by {self.customer.username}'
    
    def save(self, *args, **kwargs):
        # setting book rent end date if it is not set
        if not self.rent_end_date:
            # 14 days post the book was rented
            self.rent_end_date = self.rent_start_date + timedelta(days=14) 
        super().save(*args, **kwargs)




