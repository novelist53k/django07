from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.hashers import check_password
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "acc/index.html")

def userLogin(request):
    if request.method == "POST":
        user = authenticate(username=request.POST.get("uname"), password=request.POST.get("upass"))
        if user:
            login(request, user)
            return redirect("acc:index")
        else:
            messages.error(request, "계정 정보가 일치하지 않습니다")
    return render(request, "acc/login.html")

def userLogout(request):
    logout(request)
    messages.success(request, "로그아웃되었습니다")
    return redirect("acc:index")

def signup(request):
    if request.method == "POST":
        try:
            upic = request.FILES.get("upic")
            User.objects.create_user(username=request.POST.get("uname"), password=request.POST.get("upass"), comment=request.POST.get("ucomm"), pic=upic).save()
            return redirect("acc:index")
        except Exception as e:
            print(e)
            messages.error(request, "USERNAME이 중복되었습니다")

    return render(request, "acc/signup.html")

def profile(request):
    return render(request, "acc/profile.html")

def delete(request):
    u = request.user
    if check_password(request.POST.get("chpass"), u.password):
        u.pic.delete()
        u.delete()
        return redirect("acc:index")
    else:
        messages.error(request, "비밀번호가 일치하지 않습니다")
    return redirect("acc:profile")

def update(request):
    if request.method == "POST":
        u = request.user
        
        if u.pic:
            u.pic.delete()
        
        u.pic = request.FILES.get("upic")
        
        u.email = request.POST.get("umail")
        u.comment = request.POST.get("ucomm")

        u.save()

        messages.success(request, "정보가 수정되었습니다.")

        return redirect("acc:profile")
    return render(request, "acc/update.html")

def chpass(request):
    if check_password(request.POST.get("bpass"), request.user.password):
        request.user.set_password(request.POST.get("cpass"))
        request.user.save()
        return redirect("acc:index")
    return redirect("acc:update")

