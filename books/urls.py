from django.urls import path
from .views import BookTitleView, book_title_detail_view

app_name = 'books' # necessary for adding namespace in core:urls

urlpatterns = [
    path('', BookTitleView.as_view(), name='main'),
    path('<pk>/', book_title_detail_view, name='detail'),
]
