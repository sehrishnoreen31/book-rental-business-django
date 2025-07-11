from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home_view'),
    path('books/', include('books.urls', namespace='books'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Book Rental System'
admin.site.site_title = 'Admin'
admin.site.index_title = 'Book Rental System Administration'