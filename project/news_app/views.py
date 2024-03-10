from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, 'flatpages/default.html')

def news(request):
    data = {
        'title': 'Новости',
        'values': ['Новость 1','Новость 2','Новость 3','Новость 4','Новость 5']
    }
    return render(request, 'flatpages/news.html', data)

def about(request):
    return HttpResponse('<h2>О сайте</h2>')

def details(request):
    return render(request, 'flatpages/about.html')
