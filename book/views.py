from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from book.models import Book
from author.models import Author
from authentication.models import CustomUser
from order.models import Order

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.


def index(request):
    """View function for home page of site."""

    num_books = len(Book.get_all())
    num_authors = len(Book.get_all())
    num_orders = len(Order.get_all())
    lst_not_returned_books = Order.get_not_returned_books()
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_authors': num_authors,
        'num_orders': num_orders,
        'lst_not_returned_books': lst_not_returned_books,
        'num_visits': num_visits,
    }
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 3


class BookDetailView(generic.DetailView):
    model = Book


class BookCreate(CreateView):
    model = Book
    fields = ['name', 'description', 'count', 'authors']


class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books')



