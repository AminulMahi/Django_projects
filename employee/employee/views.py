from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from myapp.models import user_data

def home(request):
    all_data = user_data.objects.all()
    data = {'all_user_data' : all_data}
    return render(request, 'index.html', data)
# def home(request):
#     all_data = user_data.objects.all()
#     return render(request, 'index.html', {'all_user_data' : all_data})

def user(request):
    u_name = request.POST.get('name')
    # CreatingVariable = requestMethod.POSTmethod.GetMethod(ValueFromHTMLnameAttribute)
    u_email = request.POST.get('email')
    u_phone = request.POST.get('phone')
    u_image = request.FILES.get('image')
    u_video = request.FILES.get('video')

    user_obj = user_data()
    user_obj.name = u_name
    user_obj.email = u_email
    user_obj.phone = u_phone
    user_obj.image = u_image
    user_obj.video = u_video
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
    u_video = request.FILES.get('video')

    user_obj = get_object_or_404(user_data,id=id) #select single data by id from user model
    # getting objects from diifrent id
    user_obj.name = u_name
    user_obj.email = u_email
    user_obj.phone = u_phone
    user_obj.image = u_image
    user_obj.video = u_video

    user_obj.save()
    return redirect('user_home')
# save and redirect to 'user_home'= that's the home page 


def delete(request, id):
    all_data = user_data.objects.filter(id=id) #select single data by id from user model
    all_data.delete()  #delete the specific id by using delete() function
    return redirect('user_home') # then redirect to 'user_home' means home page