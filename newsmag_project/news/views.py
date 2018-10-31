from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from . import models

class NewsListView(ListView):
    model = models.News
    template_name = 'news_list.html'

class NewsDetailView(DetailView):
    model = models.News
    template_name = 'news_detail.html'

class NewsUpdateView(UpdateView):
    model = models.News
    fields = ['title', 'body', ]
    template_name = 'news_edit.html'

class NewsDeleteView(DeleteView):
    model = models.News
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')

class NewsCreateView(CreateView):
    model = models.News
    template_name = 'news_new.html'
    fields = ['title', 'body', 'author',]
