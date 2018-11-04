from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from . import models

class NewsListView(LoginRequiredMixin, ListView):
    model = models.News
    template_name = 'news_list.html'
    login_url = 'login'

class NewsDetailView(LoginRequiredMixin, DetailView):
    model = models.News
    template_name = 'news_detail.html'
    login_url = 'login'

class NewsUpdateView(LoginRequiredMixin, UpdateView):
    model = models.News
    fields = ['title', 'body', ]
    template_name = 'news_edit.html'
    login_url = 'login'

class NewsDeleteView(LoginRequiredMixin, DeleteView):
    model = models.News
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')
    login_url = 'login'

class NewsCreateView(LoginRequiredMixin, CreateView):
    model = models.News
    template_name = 'news_new.html'
    fields = ['title', 'body', ]
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
