from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic

from books.models import Book 

@method_decorator(login_required, name='dispatch')
class BookListView(generic.ListView):
    template_name = 'books/book_list.html'

    def get_queryset(self):
        """ Returns the books of the user."""
        return Book.objects.filter(user = self.request.user)
