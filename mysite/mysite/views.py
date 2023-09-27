from django.http import HttpResponse
from django.shortcuts import render

# def index(response):
#     return HttpResponse("I am ok!")
def index(request):
    return render(request, 'home.html')

def user(request):
    return render(request, 'index.html')
