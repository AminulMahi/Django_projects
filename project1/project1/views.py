from django.http import HttpResponse
from django.shortcuts import render
from .models import User
# from project2.model import User

def home(request):
    return render(request, 'index1.html')

def login(request):
    return render(request, 'index.html')
def output(request):
    return render(request, 'output.html')


    

def insert_info(request):
    # if request.method == 'POST':  # post is secure method
        nam = request.POST.get('nam')
        # CreatingVariable = requestMethod.POSTmethod.GetMethod(ValueFromHTMLnameAttribute)
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(nam)

        
        user = User(name=nam,email=email,phone=phone,messages=message)
        # object= ClassFromModel(VariableFromModel=variableFromViewFunc)
        user.save()
        return render(request, 'output.html')
