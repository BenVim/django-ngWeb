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
    now = datetime.datetime.now()
    html = "<html><body>Client DownLoad!!! %s.</body></html>" % now
    return HttpResponse(html)

def about(request):
    html = "<html><body>about ours</body></html>"
    return HttpResponse(html)

def register(request):
    html = "<html><body>register</body></html>"
    return HttpResponse(html)

def login(requset):
    html = "<html><body>login</body></html>"
    return HttpResponse(html)

def doc(request):
    html = "<html><body>doc</body></html>"
    return HttpResponse(html)