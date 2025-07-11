from django.contrib import admin
from .models import Publisher
# import-export
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.fields import Field

# resources
class PublisherResource(resources.ModelResource):
    id = Field(attribute='id', column_name='ID')
    name = Field(attribute='name', column_name='Name')
    country = Field(attribute='country', column_name='Country')
    created = Field(attribute='created', column_name='Created')
    date_created = Field(attribute='created', column_name='Date_Created')
    updated = Field(attribute='updated', column_name='Updated')
    class Meta:
        model = Publisher
        fields = ('id', 'name', 'country', 'created', 'date_created', 'updated')
        export_order = fields

    def dehydrate_date_created(self, obj):
        return obj.created.strftime('%d/%m/%y')

# admin
class PublisherAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = PublisherResource

# register
admin.site.register(Publisher, PublisherAdmin)