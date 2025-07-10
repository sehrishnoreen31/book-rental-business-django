from django.contrib import admin
from .models import Publisher
# import-export
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.fields import Field

# resources
class PublisherResource(resources.ModelResource):
    date_created = Field()
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