from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class NewsList(ListView):
    model = Post
    ordering = '-date_creation'
    template_name = 'all_news.html'
    context_object_name = 'All_News'

    # def get_context_data(self, **kwargs):
    #     amount = super().get_context_data(**kwargs)
    #     amount['all_news_quantity'] = Post
    #
    #     return amount

class OneNews(DetailView):
    model = Post
    template_name = "one_news.html"
    context_object_name = "One_News"

