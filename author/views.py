from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from author.models import Author

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 3


class AuthorDetailView(generic.DetailView):
    model = Author


class AuthorCreate(CreateView):
    model = Author
    fields = ['name', 'surname', 'patronymic']


class AuthorUpdate(UpdateView):
    model = Author
    fields = '__all__'


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')