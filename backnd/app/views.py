from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import logout,authenticate,login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.form import *
from django.contrib import messages
from app.models import *
from django.db import connection

# Navigation propose 
def Header(request):
    return render(request,"admin/header.html")

# logout user 
@login_required
def LogoutUser(request):
    logout(request)
    return redirect('/')

#  senior teacher dashboard 
@login_required
def AdminDash(request):
    fm = userCreateForm()  # check in form.py
    data = User.objects.all()
    user_type_fm = User_type_creation_fm()
    
    if request.method == "POST":
        fm = userCreateForm(request.POST)
        user_type_fm =  User_type_creation_fm(request.POST)

        if fm.is_valid():
            fm.instance.email = request.POST['username']
            user= request.POST['username']
            password = request.POST['username']
            userFm = fm.save()
            userFm.set_password(userFm.password)
            userFm.save()
            
     
            if user_type_fm.is_valid():
                user_type_fm.instance.user = User.objects.get(username = user)
                user_type_fm.save()
                messages.success(request,"user create successfully !")
        else:
            messages.error(request,"Please enter valid data")
    return render(request,'senior_teacher/dashboard.html',{'fm':fm,'user_type_fm':user_type_fm,'user':data})


# login user
def LoginUser(request):
    if request.user.is_authenticated:
        if request.user.is_superuser or user_type.objects.get(user = request.user).type == "1":
            return redirect('senior_teacher_dash')
        elif user_type.objects.get(user = request.user).type == "2":
            return redirect('normal_user_dash')
        elif user_type.objects.get(user = request.user).type == "3":
            return redirect('normal_user_dash')
        else:
            return HttpResponse(user_type.objects.get(user = request.user))
    else:
        if request.method == "POST":
            username = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(username = username,password=password)
            if user is not None:
                login(request,user)
                return redirect("/")
            else:
                messages.error(request,"email and password doesn't match please try again!")
        return render(request,'loginuser.html')
    

# senior teacher can edit the user 
def UserEdit(request,id):
    fm = userChangeFm(instance=User.objects.get(id = id)) # check in form.py
    try:
        user_type_fm = User_type_creation_fm(instance = user_type.objects.get(user = User.objects.get(id = id)))
    except:
        user_type_fm = User_type_creation_fm()
    if request.method == "POST":
        fm = userChangeFm(request.POST,instance=User.objects.get(id = id))
        if fm.is_valid():
            user_fm = fm.save()
            user_fm.save()
        
            messages.success(request,'Changed data successful')

        try:
            user_type_fm = User_type_creation_fm(request.POST ,instance = user_type.objects.get(user = User.objects.get(id = id)))
            if user_type_fm.is_valid():
                user_type_fm.save()
            else:
                messages.error(request,'Please enter the valid data !')
        except:
            user_type_fm = User_type_creation_fm(request.POST)
            user_type_fm.instance.user = User.objects.get(id = id)
            user_type_fm.save()
        

    return render(request,'senior_teacher/edit_user.html',{'fm':fm,'user_type_fm':user_type_fm})


# senior teacher can delete the user 
def userDelete(request,id):
    user = User.objects.get(id = id)
    user.delete()
    return redirect('home')

def FormFieldView(request):
    if request.user.is_superuser or user_type.objects.get(user = request.user).type == "1" :
        data = HtmlFormModel.objects.all()
        return render(request,"senior_teacher/form_field.html",{'data':data})
    else:
        return HttpResponse("<h1> Not a authenticate user to access this page</h1>")
    


  
def HtmlFormSaveView(request):
    if request.user.is_superuser or user_type.objects.get(user = request.user).type == "1" :
        if(HtmlFormModel.objects.filter(table_name = str(request.GET['table_name_input'])).exists()):
            messages.error(request,"Table already exists.!")
            return redirect('form_field')
        else:
            query = f"CREATE TABLE _{str(request.GET['table_name_input'])}(id bigint PRIMARY KEY AUTO_INCREMENT, {str(request.GET['query_fields_input'])},htmlno bigint,foreign key(htmlno) references app_htmlformmodel(id) on delete cascade);"
            
            try:
                cursor = connection.cursor()
                cursor.execute(query)
                cursor.close()
                data = HtmlFormModel(html = str(request.GET['html_fields_input']),table_name = str(request.GET['table_name_input']),user = request.user)
                data.save()
                messages.success(request,'Form create successful')
            except:
                messages.error(request,"Something error try again please check the condition before create form")
                print("================================>>",query)
                return redirect('form_field')
            
        return redirect('html_form_list')
    else:
        return HttpResponse("You are not a valid user to access this!")

def HtmlFormListView(request):
    data = {
        'model' : HtmlFormModel.objects.all().order_by('-id')
    }
    return render(request,'senior_teacher/form_list.html',data)

def HtmlInputView(request,id):
    data = {
        'data':HtmlFormModel.objects.get(pk = id)
    }
    return render(request,'senior_teacher/form_view.html',data)

def RemoveFormView(request,tab):
   
    query = f"DROP TABLE _{tab};"
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        cursor.close()
        HtmlFormModel.objects.get(table_name = tab).delete()
        messages.warning(request,'Successfully delate form')
    except:
        return HttpResponse(query)
    return redirect('html_form_list')

# NormalUser
def UserDash(request):
    data = {
        'user_type':user_type.objects.get(user = request.user).type
    }
    return render(request,'normal_user/dashboard.html',data)

def UserFormList(request):
    data = {
        'model' : HtmlFormModel.objects.all().order_by('-id')
    }
    return render(request,'normal_user/form.html',data)


def UserFormView(request,id):
    data = {
        'data':HtmlFormModel.objects.get(pk = id)
    }
    return render(request,'normal_user/form_view.html',data)

def Form_submit(request):
    # print('================>>>',request.GET['table_name'])
    # print('================>>>',request.GET['pass_data_inp'])
    query = f"INSERT INTO {request.GET['table_name']} VALUES(null,{request.GET['pass_data_inp']},null);"
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        cursor.close()
        messages.success(request,"data added successful")
    except:
        return HttpResponse(query)
    return redirect(request.META.get('HTTP_REFERER'))



        
        

