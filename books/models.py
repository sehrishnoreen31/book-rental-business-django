from django.db import models
from django.urls import reverse
# related models
from publishers.models import Publisher
from authors.models import Author
from rentals.choices import STATUS_CHOICES

# for slugs
from django.utils.text import slugify

# for unique book ids
import uuid

# for qr code
import qrcode
from io import BytesIO
from django.core.files import File

# Create your models here.
class BookTitle(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    # on to many relationships
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # get books assiciated with a book title - reverse relationship
    @property
    def books(self):
        return self.book_set.all()
    
    def get_absolute_url(self):
        return reverse("books:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"Book Position: {self.title}"
    
    # overriding save method
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Book(models.Model):
    title = models.ForeignKey(BookTitle, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=24, blank=True)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
    
    @property
    def status(self):
        # reverse relationship
        if len(self.rental_set.all()) > 0:
            statuses = dict(STATUS_CHOICES)
            return statuses[self.rental_set.first().status]
        return False

    # overriding save method
    def save(self, *args, **kwargs):
        if not self.isbn:
            # enerating unique book id
            self.isbn = str(uuid.uuid4()).replace("-", "")[:24].lower()

            # generating book qr code image from book_id
            qr = qrcode.QRCode(
                        version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=10,
                        border=4,
                    )
            qr.add_data(self.isbn)
            qr.make(fit=True)
            qr_code_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
            # give a name to image file
            fname = f'qr-code-{self.title}.png'
            # initializing buffer for an in-memory file, (not storing in disk)
            # It will avoid creating a temporary file on disk and make the process fast and efficient
            buffer = BytesIO() 
            # save image in PNG format
            qr_code_img.save(buffer, 'PNG')
            # save new qr code image in qr_code variable
            self.qr_code.save(fname, File(buffer), save=False)


        super().save(*args, **kwargs)
