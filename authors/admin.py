from django.contrib import admin
from .models import Author
# import export
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.fields import Field

# resorces
class AuthorResource(resources.ModelResource):
    id = Field(attribute='id', column_name='ID')
    name = Field(attribute='name', column_name='Name')
    
    class Meta:
        model = Author
        fields = ('id', 'name')
        export_order = fields

# register, admin
@admin.register(Author)
class AuthorAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = AuthorResource
