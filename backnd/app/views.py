from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import logout,authenticate,login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.form import userCreateForm,userChangeFm
from django.contrib import messages
from app.models import User

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
    data = User.objects.all().order_by('user_type')
    if request.method == "POST":
        fm = userCreateForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"user create successfully !")
        else:
            messages.error(request,"Please enter valid data")
    return render(request,'senior_teacher/dashboard.html',{'fm':fm,'user':data})


# login user
def LoginUser(request):
    if request.user.is_authenticated:
        if request.user.user_type == '1':
            return redirect('senior_teacher_dash')
    else:
        if request.method == "POST":
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(email = email,password=password)
            if user is not None:
                login(request,user)
                return redirect("/")
            else:
                messages.error(request,"email and password doesn't match please try again!")
        return render(request,'loginuser.html')
    

# senior teacher can edit the user 
def UserEdit(request,id):
    fm = userChangeFm(instance=User.objects.get(id = id)) # check in form.py
    if request.method == "POST":
        fm = userChangeFm(request.POST,instance=User.objects.get(id = id)) # check in form.py
        fm.save()
        messages.success(request,'Changed data successful')
    else:
        messages.error(request,'Please enter the valid data !')

    return render(request,'senior_teacher/edit_user.html',{'fm':fm})


# senior teacher can delete the user 
def userDelete(request,id):
    user = User.objects.get(id = id)
    user.delete()
    return redirect('home')
    

        

