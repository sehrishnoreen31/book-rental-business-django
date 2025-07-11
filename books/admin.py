from django.contrib import admin
from .models import Book, BookTitle
# import export
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.fields import Field

# resources
class BookResource(resources.ModelResource):
    title = Field(attribute='title', column_name='Book_Title')
    status = Field(attribute='status', column_name='Status')
    publisher = Field(attribute='publisher', column_name='Publisher')
    isbn = Field(attribute='isbn', column_name='ISBN')
    qr_code = Field(attribute='qr_code', column_name='QR_Code')
    created = Field(attribute='created', column_name='Date_Created')
    updated = Field(attribute='updated', column_name='Date_Updated')
    
    class Meta:
        model = Book
        fields = ('title', 'isbn', 'publisher', 'qr_code', 'status', 'created', 'updated')
        export_order = fields
    
    # title
    def dehydrate_title(self, obj):
        return obj.title.title
    
    # status
    def dehydrate_status(self, obj):
        return obj.status
    # publisher
    def dehydrate_publisher(self, obj):
        return obj.title.publisher.name

# Register, admin
@admin.register(Book)
class BookAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = BookResource
    readonly_fields = ('isbn', 'qr_code')

@admin.register(BookTitle)
class BookTitleAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)