from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

articles = {
    'sports': 'Sports Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page'
}

def news_view(request,topic):
    try:
        return HttpResponse(articles[topic]) if topic != '0' else HttpResponseRedirect('/first_app/sports')
    except:
        raise Http404("404 GENERIC ERROR")

def add_view(request,num1,num2):
    add_result = num1 + num2
    result = f"{num1} + {num2} = {add_result}"
    return HttpResponse(result)

def num_page_view(request,num_page):
    topics_list = list(articles.keys())
    topic = topics_list[num_page]

    return HttpResponseRedirect(reverse('topic-page',args=[topic]))