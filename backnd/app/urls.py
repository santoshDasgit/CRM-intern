
from django.contrib import admin
from django.urls import path
from . import views
from . import views_user


urlpatterns = [
    path('', views.LoginUser,name='home'),
    path('logout/',views.LogoutUser,name='logout'),
    path('senior_teacher/dashboard',views.AdminDash,name='senior_teacher_dash'),
    path('senior_teacher/edit_user/<id>',views.UserEdit,name='senior_teacher_edit_user'),
    path('senior_teacher/delete_user/<id>',views.userDelete,name='senior_teacher_delete_user'),
    path('senior_teacher/form_field',views.FormFieldView,name='form_field'),
    path('senior_teacher/html_form_save',views.HtmlFormSaveView,name='html_form_save'),
    path('senior_teacher/html_form_list',views.HtmlFormListView,name='html_form_list'),
    path('senior_teacher/html_form_view/<id>',views.HtmlInputView,name='html_form_view'),
     path('senior_teacher/remove_form_view/<tab>',views.RemoveFormView,name='remove_form_view'),

    #  normal user 
    path('normal_user/dashboard/',views.UserDash,name='normal_user_dash'),
    path('normal_user/form/',views.UserFormList,name='normal_user_form'),
    path('normal_user/form_view/<id>',views.UserFormView,name='normal_user_form_view'),
    path('normal_user/form_submit/',views.Form_submit,name='normal_user_form_submit')
]