from datetime import time
import hashlib
from django import forms
import time

# Create your views here.
from django.shortcuts import render

from ngrokApp.models import Memeber


class RegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
    verifyPassword = forms.CharField()


def login(request):
    Memeber.objects.all()
    context = {}
    context['hello'] = "abc"
    return render(request, 'login.html', context)


def register(request):
    if request.method == "POST":
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():
            email = registerForm.cleaned_data['email']
            password = registerForm.cleaned_data['password']
            verifyPassword = registerForm.cleaned_data['verifyPassword']

            if password == verifyPassword:
                t = time.time()
                p = Memeber(email=email, password=md5(password), token=md5(email+str(t)), addTime=int(t))
                print(p.save())
            else:
                print("password error")
        else:
            print("fuck")

    context = {}
    context['hello'] = "abc"
    return render(request, 'register.html', context)

def md5(str):
    m2 = hashlib.md5()
    m2.update(str.encode('utf8'))
    return m2.hexdigest()