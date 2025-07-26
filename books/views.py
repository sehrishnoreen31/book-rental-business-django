from django.shortcuts import render, get_object_or_404
from .models import BookTitle, Book
from .forms import BookTitleForm
from django.views.generic import ListView, FormView

# class based view
class BookTitleView(ListView, FormView):
    model = BookTitle
    template_name = 'books/main.html'
    context_object_name = 'list_of_book_titles'
    form_class = BookTitleForm
    
    # overriding the get success url
    def get_success_url(self):
        return self.request.path
    
    # save form data to database
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    # form validation
    def form_invalid(self, form):
        self.object_list = self.get_queryset()
        return super().form_invalid(form)

    # overriding the get_queryset
    def get_queryset(self):
        return BookTitle.objects.all().order_by('-created')

def book_title_detail_view(request, **kwargs):
    pk = kwargs.get('pk')
    book_detail = BookTitle.objects.get(pk=pk)
    context = {
        'book_detail': book_detail
    }
    return render(request, 'books/detail.html', context)

