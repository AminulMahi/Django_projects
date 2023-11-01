from django.shortcuts import render, redirect, get_object_or_404
from adminapp.models import Main
# Create your views here.

# # main page index and getting data from DB to main page
# def index(request):
#     all_data = Main.objects.all()
#     data = {'all_user_data' : all_data}
#     return render(request, 'index.html', data)

# #admin page ndex and getting data from DB to main page
# def admin_index(request):
#     all_data = Main.objects.all()
#     data = {'all_user_data' : all_data}
#     return render(request, 'admin/admin.html', data)

# # insert data by user to main page
# def user(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         l_name = request.POST.get('l_name')
#         address = request.POST.get('address')
#         phone = request.POST.get('phone')
#         email = request.POST.get('email')
#         description = request.POST.get('description')

#     obj = Main(
#             name = name,
#             l_name = l_name,
#             email = email,
#             address = address,
#             phone = phone,
#             description = description,
#         )
#     obj.save()
#     return redirect('index')

# # update data by user to main page
# def update(request, id):
#     if request.method == 'POST':
#         # id = request.POST.get('id')
#         name = request.POST.get('name')
#         l_name = request.POST.get('l_name')
#         address = request.POST.get('address')
#         phone = request.POST.get('phone')
#         email = request.POST.get('email')
#         description = request.POST.get('description')

#     obj = Main(
#             id = id,
#             name = name,
#             l_name = l_name,
#             email = email,
#             address = address,
#             phone = phone,
#             description = description,
#         )
#     obj.save()
#     return redirect('index')

# # Delete data by user to main page
# def delete(request, id):
#     all_data = Main.objects.filter(id=id) #select single data by id from user model
#     all_data.delete()
#     return redirect('index')