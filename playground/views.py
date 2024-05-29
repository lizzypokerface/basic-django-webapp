# NOTE: A Django view is a request handler that takes a web request and returns a web response.

from django.shortcuts import render

# from django.http import HttpResponse

# Create your views here.


def say_hello(request):
    return render(request, "hello.html", {"name": "Glenn"})
