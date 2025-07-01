from django.contrib import admin
from .models import Rental
# Register your models here.
@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    pass