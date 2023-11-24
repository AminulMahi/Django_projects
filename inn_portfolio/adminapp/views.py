from django.shortcuts import render, redirect
from django.http import HttpResponse
from adminapp.models import Main, Experience, Education, Skills, Interest, Awards
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

# main page index and getting data from DB to main page

def index(request):
    all_data = Main.objects.all()
    all_data1 = Experience.objects.all()
    all_data2 = Education.objects.all()
    all_data3 = Skills.objects.all()
    all_data4 = Interest.objects.all()
    all_data5 = Awards.objects.all()
    data = {
        'all_user_data' : all_data,
        'all_exp_data' : all_data1,
        'all_edu_data' : all_data2,
        'all_skill_data' : all_data3,
        'all_int_data' : all_data4,
        'all_awa_data' : all_data5,
        }
    return render(request, 'index.html', data)

#Signup system
def SignUp(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1!= pass2:
            return HttpResponse("Your password and confirm pass is not same. Try again!")
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('signup')
    return render(request, 'admin/signup.html')

#Login function
def LogIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('admin_index')
        else:
            return HttpResponse("Your username and passwrod is wrong! Try again!")
    return render(request, 'admin/login.html')

#logout function
def LogOutPage(request):
    logout(request)
    return redirect('/')

#admin page ndex and getting data from DB to main page
@login_required(login_url='login')
def admin_index(request):
    all_data = Main.objects.all()
    data = {'all_user_data' : all_data}
    return render(request, 'admin/admin.html', data)

# insert data by user to main page
def user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        l_name = request.POST.get('l_name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        f_url = request.POST.get('f_url')
        l_url = request.POST.get('l_url')
        t_url = request.POST.get('t_url')
        g_url = request.POST.get('g_url')

    obj = Main(
            name = name,
            l_name = l_name,
            email = email,
            address = address,
            phone = phone,
            description = description,
            image = image,
            f_url = f_url,
            l_url = l_url,
            t_url = t_url,
            g_url = g_url,
    )
    obj.save()
    return redirect('index')

# update data by user to main page
def update(request, id):
    if request.method == 'POST':
        # id = request.POST.get('id')
        name = request.POST.get('name')
        l_name = request.POST.get('l_name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        description = request.POST.get('description')
        image = request.FILES.get('image')

    obj = Main(
            id = id,
            name = name,
            l_name = l_name,
            email = email,
            address = address,
            phone = phone,
            description = description,
            image = image,
        )
    obj.save()
    return redirect('index')

# Delete data by user to main page
def delete(request, id):
    all_data = Main.objects.filter(id=id) #select single data by id from user model
    all_data.delete()
    return redirect('admin_index')

# Experience page views
# insert page

@login_required(login_url='login')
def exp(request):
    all_data = Experience.objects.all()
    data = {'all_exp_data' : all_data}
    return render(request, 'admin/Experience.html', data)

def insert(request):
    if request.method == 'POST':
        heading = request.POST.get('heading')
        sub_heading = request.POST.get('sub_heading')
        date = request.POST.get('date')
        description = request.POST.get('description')

    obj = Experience(
            heading = heading,
            sub_heading = sub_heading,
            date = date,
            description = description,
        )
    obj.save()
    return redirect('exp')

def delete_exp(request, id):
    all_data = Experience.objects.filter(id=id) #select single data by id from user model
    all_data.delete()
    return redirect('exp')

# Education page views
@login_required(login_url='login')
def edu(request):
    all_data = Education.objects.all()
    data = {'all_edu_data' : all_data}
    return render(request, 'admin/Education.html', data)

# insert data to education page

def edu_insert(request):
    if request.method == 'POST':
        u_name = request.POST.get('u_name')
        u_title = request.POST.get('u_title')
        u_subject = request.POST.get('u_subject')
        u_gpa = request.POST.get('u_gpa')
        u_date = request.POST.get('u_date')

    obj = Education(
            u_name = u_name,
            u_title = u_title,
            u_subject = u_subject,
            u_gpa = u_gpa,
            u_date = u_date,
        )
    obj.save()
    return redirect('edu')

def delete_edu(request, id):
    all_data = Education.objects.filter(id=id) #select single data by id from user model
    all_data.delete()
    return redirect('edu')

# skills page views
@login_required(login_url='login')
def skills(request):
    all_data = Skills.objects.all()
    data = {'all_skill_data' : all_data}
    return render(request, 'admin/Skills.html', data)

def skill_insert(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        workflow = request.POST.get('workflow')

    obj = Skills(
            image = image,
            workflow = workflow
        )
    obj.save()
    return redirect('skills')   

def delete_skill(request, id):
    all_data = Skills.objects.filter(id=id) #select single data by id from user model
    all_data.delete()
    return redirect('skills')

# interest page views
@login_required(login_url='login')
def interest(request):
    all_data = Interest.objects.all()
    data = {'all_int_data' : all_data}
    return render(request, 'admin/Interest.html', data)

def int_interest(request):
    if request.method == 'POST':
        interest = request.POST.get('interest')

    obj = Interest(
            interest = interest,
        )
    obj.save()
    return redirect('interest')

def delete_int(request, id):
    all_data = Interest.objects.filter(id=id) #select single data by id from user model
    all_data.delete()
    return redirect('interest')

# Award page views
@login_required(login_url='login')
def awards(request):
    all_data = Awards.objects.all()
    data = {'all_awa_data' : all_data}
    return render(request, 'admin/Awards.html', data)

def awa_insert(request):
    if request.method == 'POST':
        awards = request.POST.get('awards')

    obj = Awards(
            awards = awards,
        )
    obj.save()
    return redirect('awards')

def delete_awa(request, id):
    all_data = Awards.objects.filter(id=id) #select single data by id from user model
    all_data.delete()
    return redirect('awards')