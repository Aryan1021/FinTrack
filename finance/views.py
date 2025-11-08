from django.shortcuts import render, HttpResponse
from django.views import View

def home(request):
    return HttpResponse("<h1>Hello Django</h1>")

class Homeview(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Hello Django Class</h1>")