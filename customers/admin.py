from django.contrib import admin
from .models import Customer
# import export
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.fields import Field

# resources
class CustomerResource(resources.ModelResource):
    # customize additional info and books data output
    first_name = Field(attribute='first_name', column_name='First_Name')
    last_name = Field(attribute='last_name', column_name='Last_Name')
    username = Field(attribute='username', column_name='Username')
    additional_info = Field(attribute='additional_info', column_name='Additional_Info')
    rating = Field(attribute='rating', column_name='Rating')
    books = Field(attribute='books', column_name='Books')
    book_count = Field(attribute='book_count', column_name='Book_Count')
    
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'username', 'additional_info', 'rating', 'books', 'book_count')
        export_order = fields

    # additional info column modifications
    def dehydrate_additional_info(self, obj):
        if len(obj.additional_info) == 0:
            return '-'
        elif len(obj.additional_info) <= 5:
            return obj.additional_info
        else:
            # get first five characters of additional info
            txt_list = obj.additional_info.split(' ')[:5]
            return ' '.join(txt_list) + '...'
        
    # books column modifications
    def dehydrate_books(self, obj):
        book = [x.isbn for x in obj.books.all()]
        return ', '.join(book)

# register, admin
@admin.register(Customer)
class CustomerAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = CustomerResource