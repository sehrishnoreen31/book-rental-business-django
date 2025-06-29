from django.db import models
from publishers.models import Pubisher
from authors.models import Author
from django.utils.text import slugify
import uuid
# Create your models here.
class BookTitle(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(blank=True)
    publisher = models.ForeignKey(Pubisher, on_delete=models.CASCADE)
    # on to many relationships
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Book Position: {self.title}"
    
    # overriding save method
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Book(models.Model):
    title = models.ForeignKey(BookTitle, on_delete=models.CASCADE)
    book_id = models.CharField(max_length=24, blank=True)
    # qr code
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    # overriding save method
    def save(self, *args, **kwargs):
        if not self.book_id:
            self.book_id = str(uuid.uuid4()).replace("-", "")[:24].lower()
        super().save(*args, **kwargs)
