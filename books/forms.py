from django import forms
from .models import BookTitle

class BookTitleForm(forms.ModelForm):
    class Meta:
        model = BookTitle
        fields = ('title', 'author', 'publisher')
    
    # form validation 
    def clean(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            self.add_error('title', 'title is too short')
        book_title_exists = BookTitle.objects.filter(title__iexact=title).exists()
        if book_title_exists:
            self.add_error('title', 'Title already exists')
