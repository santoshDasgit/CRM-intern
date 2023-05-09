
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginUser,name='home'),
    path('logout/',views.LogoutUser,name='logout'),
    path('senior_teacher/dashboard',views.AdminDash,name='senior_teacher_dash'),
    path('senior_teacher/edit_user/<id>',views.UserEdit,name='senior_teacher_edit_user'),
    path('senior_teacher/delete_user/<id>',views.userDelete,name='senior_teacher_delete_user')
]