from django.contrib import admin
from django.urls import path, include

from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    # admin main page
    path('index/admin/', views.admin_index, name='admin_index'),
    path('index/user/', views.user, name='user_index'),
    path('index/update/<str:id>', views.update, name='update_index'),
    path('index/delete/<str:id>', views.delete, name='delete_item'),

    # experience page
    path('index/experience/', views.exp, name='exp'),
    path('index/insert/', views.insert, name='insert_index'),
    path('index/exp/delete/<str:id>', views.delete_exp, name='delete_exp_item'),

    #education page
    path('index/education/', views.edu, name='edu'),
    path('index/edu_insert/', views.edu_insert, name='edu_insert_index'),
    path('index/edu/delete/<str:id>', views.delete_edu, name='delete_edu_item'),

    #Skills page
    path('index/skills/', views.skills, name='skills'),
    path('index/skill_insert/', views.skill_insert, name='skill_insert'),
    path('index/skill/delete/<str:id>', views.delete_skill, name='delete_skill_item'),
    
    #interest page
    path('index/interest/', views.interest, name='interest'),
    path('index/int_interest/', views.int_interest, name='int_interest'),
    path('index/int/delete/<str:id>', views.delete_int, name='delete_int_item'),

    #award page
    path('index/awards/', views.awards, name='awards'),
    path('index/awa_insert/', views.awa_insert, name='awa_insert'),
    path('index/awa/delete/<str:id>', views.delete_awa, name='delete_awa_item'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)