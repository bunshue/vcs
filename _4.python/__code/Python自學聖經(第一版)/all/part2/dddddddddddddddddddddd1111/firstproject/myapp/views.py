from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random  # 加入 random 套件


# Create your views here.

def sayhello(request):
    return HttpResponse("Hello Django!")

def hello2(request,username):
    return HttpResponse("Hello " + username)
   
def hello3(request,username):
    now=datetime.now()
    return render(request,"hello3.html",locals())
   
def hello4(request,username):
    now=datetime.now()
    return render(request,"hello4.html",locals())
   
def dice(request):
    no1=random.randint(1,6)   # 1~6
    no2=random.randint(1,6)   # 1~6
    no3=random.randint(1,6)   # 1~6
    # 使用 locals()傳遞所有的區域變數 
    return render(request,"dice.html",locals())   

def show(request):
    person1={"name":"Amy","phone":"049-1234567","age":20}
    person2={"name":"Jack","phone":"02-4455666","age":25}
    person3={"name":"Nacy","phone":"04-9876543","age":17}
    persons=[person1,person2,person3]
    return render(request,"show.html",locals())

def djget(request):
    name = request.GET['name']
    city = request.GET['city']
    return render(request,"djget.html",locals())

def djpost(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username=='david' and password=='1234':
            return HttpResponse('歡迎光臨本網站！')
        else:
            return HttpResponse('帳號或密碼錯誤！')
    else:
        return render(request,"djpost.html",locals())



