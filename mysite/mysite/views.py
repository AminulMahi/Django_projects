from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# def index(response):
#     return HttpResponse("I am ok!")
def index(request):
    return render(request, 'home.html')

def user(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    return HttpResponse(password)

def user_form(request):
    return render(request, 'user.html')

def login(request):
    return HttpResponseRedirect('user.html/')