from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from myapp.models import user_data

def home(request):
    all_data = user_data.objects.all()
    data = {'all_user_data' : all_data}
    return render(request, 'index.html', data)

def user(request):
    u_name = request.POST.get('name')
    u_email = request.POST.get('email')
    u_phone = request.POST.get('phone')
    u_image = request.FILES.get('image')
    user_obj = user_data()
    user_obj.name = u_name
    user_obj.email = u_email
    user_obj.phone = u_phone
    user_obj.image = u_image
    user_obj.save()
    return redirect('user_home')

def edit_index(request,id):
    all_data = user_data.objects.get(id=id)
    data = {'all_user_data' : all_data}
    return render(request, 'edit.html', data)

def update(request):
    id = request.POST.get('id')
    u_name = request.POST.get('name')
    u_email = request.POST.get('email')
    u_phone = request.POST.get('phone')
    u_image = request.FILES.get('image')

    user_obj = get_object_or_404(user_data,id=id)
    user_obj.name = u_name
    user_obj.email = u_email
    user_obj.phone = u_phone
    user_obj.image = u_image
    user_obj.save()
    return redirect('user_home')