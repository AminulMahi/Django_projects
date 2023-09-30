from django.http import HttpResponse
from django.shortcuts import render
from project2.models import User

def home(request):
    return render(request, 'index1.html')

def login(request):
    return render(request, 'index.html')
def output(request):
    return render(request, 'output.html')


    

def insert_info(request):
    if request.method == 'POST':
        nam = request.POST.get('nam')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(nam)

        
        user = User(name=nam,email=email,phone=phone,messages=message)
        user.save()
        return render(request, 'output.html')