from django.db import models
import uuid
from django_countries.fields import CountryField
# Create your models here.
class Pubisher(models.Model):
    name = models.CharField(max_length=500)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # pip install django-counties fr below field
    country = CountryField(blank_label="Select Country")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name} from {self.country}"