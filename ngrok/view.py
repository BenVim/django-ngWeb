import datetime

from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("hello world!")


def index(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'index.html', context)

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def client_download(request):
    context = {}
    context['hello'] = "abc"
    return render(request, 'download.html', context)

def about(request):
    context = {}
    context['hello'] = "abc"
    return render(request, 'about.html', context)

def register(request):
    context = {}
    context['hello'] = "abc"
    return render(request, 'register.html', context)

def login(requset):
    context = {}
    context['hello'] = "abc"
    return render(requset, 'login.html', context)

def doc(request):
    context = {}
    context['hello'] = "abc"
    return render(request, 'docment.html', context)


def qq(request):
    context = {}
    context['hello'] = "abc"
    return render(request, 'qq.html', context)

def forget(request):
    context = {}
    context['hello'] = "abc"
    return render(request, 'forget.html', context)