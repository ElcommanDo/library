from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Member

from django.contrib.auth.decorators import user_passes_test
# Create your views here.
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

def create_super_admin(request):
    if request.method=="POST":
        data = request.POST
        user = User()
        user.username = data['username']
        # user.first_name = data['first_name']
        # user.last_name = data['last_name']
        # user.email = data['email']
        user.set_password(data['password'])
        user.is_superuser = True
        user.save()
        messages.success(request,'تمت اضافه مدير موقع بنجاح')
        return redirect('home')


@user_passes_test(lambda u: u.is_superuser)
def create_admin(request):
    if request.method=="POST":
        data = request.POST
        old = User.objects.filter(username=data['username'])
        if old:
            messages.warning(request,'هذا المستخدم موجود بالفعل')
            return redirect('show_users')
        user = User()
        user.username = data['username']
        # user.first_name = data['fname']
        # user.last_name = data['lname']
        user.email = data['email']
        user.is_staff = True
        user.set_password(data['password'])
        user.save()
        messages.success(request,'تمت اضافه المستخدم بنجاح')
        return redirect('show_users')

@user_passes_test(lambda u: u.is_superuser)
def create_member(request):
    if request.method=="POST":
        data = request.POST
        if User.objects.filter(username=data['username']):
           messages.warning(request,'هذا العضو موجود بالفعل')
           return redirect('show_members')
        member = Member()
        user = User()
        user.username = data['username']
        # user.first_name = data['fname']
        # user.last_name = data['lname']
        user.email = data['email']
        user.set_password(data['password'])
        user.is_staff = False
        user.save()
        member.user = user
        member.phone = data['phone']
        member.address = data['address']
        member.save()
        messages.success(request,'تمت اضافه العضو بنجاح')
        return redirect('show_members')



def login_admin(request):
    user = request.user
    if user in User.objects.all() and user.is_active:
        return redirect('home') 
    if request.method == "POST":
        data = request.POST
        user = authenticate(request,username=data['username'],password=data['pass'])
        print(user)
        if user and user.is_staff:
            login(request,user)
            return redirect('home')
        elif user and not user.is_staff:
            login(request,user)
            return redirect('borrow_books')
        else:
            messages.warning(request,'there is something wrong')
            return redirect('login')

        

    return render(request,'accounts/login.html',{})




def logout_admin(request):
    logout(request)
    return redirect('login')



def admin_dash(request):
    
    return render(request,'employee/admin.html',{})



def show_members(request):
    members = Member.objects.all()
    return render(request,'accounts/show_members.html',{'members':members})

def show_users(request):
    users = User.objects.filter(is_superuser=False,is_staff=True)
    return render(request,'accounts/show_users.html',{'users':users})
@user_passes_test(lambda u: u.is_superuser)
def delete_admin(request,id):
   user = User.objects.get(id=id)
   user.delete()
   messages.success(request,'تم حذف المستخدم بنجاح')
   return redirect('show_users')
@user_passes_test(lambda u: u.is_superuser)
def delete_member(request,id):
   member = Member.objects.get(id=id)
   user = member.user
   member.delete()
   user.delete()
   messages.success(request,'تم حذف العضو بنجاح')
   return redirect('show_members')

@user_passes_test(lambda u: u.is_superuser)
def update_member(request,id):
    if request.method=="POST":
        data = request.POST
        member = Member.objects.get(id=id)
        member.user.username = data['username']
        # user.first_name = data['fname']
        # user.last_name = data['lname']
        member.user.email = data['email']
        member.user.set_password(data['password'])
        member.user.is_staff = False
        member.user.save()
        member.phone = data['phone']
        member.address = data['address']
        member.save()
        messages.success(request,'تمت تعديل العضو بنجاح')
        return redirect('show_members')

@user_passes_test(lambda u: u.is_superuser)
def update_admin(request,id):
    if request.method=="POST":
        data = request.POST
        user = User.objects.get(id=id)
        user.username = data['username']
        # user.first_name = data['fname']
        # user.last_name = data['lname']
        user.email = data['email']
        user.set_password(data['password'])
        user.save()
        messages.success(request,'تمت تعديل المستخدم بنجاح')
        return redirect('show_users')
