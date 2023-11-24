from django.contrib import admin
from django.urls import path, include

from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin2/', admin.site.urls),
    path('', views.index, name='index'),
    #signup page
    path('signup/',views.SignUp, name='signup'),
    #login page
    path('login/',views.LogIn, name='login'),
    #logout page
    path('logout/', views.LogOutPage, name='logout'),
    # admin main page
    path('admin/', views.admin_index, name='admin_index'),
    path('user/', views.user, name='user_index'),
    path('update/<str:id>', views.update, name='update_index'),
    path('delete/<str:id>', views.delete, name='delete_item'),

    # experience page
    path('experience/', views.exp, name='exp'),
    path('insert/', views.insert, name='insert_index'),
    path('exp/delete/<str:id>', views.delete_exp, name='delete_exp_item'),

    #education page
    path('education/', views.edu, name='edu'),
    path('edu_insert/', views.edu_insert, name='edu_insert_index'),
    path('edu/delete/<str:id>', views.delete_edu, name='delete_edu_item'),

    #Skills page
    path('skills/', views.skills, name='skills'),
    path('skill_insert/', views.skill_insert, name='skill_insert'),
    path('skill/delete/<str:id>', views.delete_skill, name='delete_skill_item'),
    
    #interest page
    path('interest/', views.interest, name='interest'),
    path('int_interest/', views.int_interest, name='int_interest'),
    path('int/delete/<str:id>', views.delete_int, name='delete_int_item'),

    #award page
    path('awards/', views.awards, name='awards'),
    path('awa_insert/', views.awa_insert, name='awa_insert'),
    path('awa/delete/<str:id>', views.delete_awa, name='delete_awa_item'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)