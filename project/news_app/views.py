from django.shortcuts import render, redirect
from .models import Articles
from django.http import HttpResponse
from django.views.generic import DetailView

def index(request):
    return render(request, 'flatpages/default.html')

def news(request):
    news = Articles.objects.order_by("-date")
    return render(request, 'flatpages/news.html', {'news':news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'flatpages/details_view.html'
    context_object_name = 'article'

def news1(request):
    news = Articles.objects.last()
    return render(request, 'flatpages/1.html', {'news1':news})

def about(request):
    return HttpResponse('<h2>О сайте</h2>')

def details(request):
    return render(request, 'flatpages/about.html')


