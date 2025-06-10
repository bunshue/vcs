from django.shortcuts import render
from studentsapp.models import student

def listone(request): 
	try: 
		unit = student.objects.get(cName="李采茜") #讀取一筆資料
	except:
  		errormessage = " (讀取錯誤!)"
	return render(request, "listone.html", locals())

def listall(request):  
	students = student.objects.all().order_by('id')  #讀取資料表, 依 id 遞增排序
	return render(request, "listall.html", locals())
	
def insert(request):  #新增資料
    if request.method == 'POST':
        cName = request.POST['name']
        cSex =  request.POST['sex']
        cBirthday =  request.POST['birthday']
        cEmail = request.POST['email']
        cPhone =  request.POST['phone']
        cAddr =  request.POST['addr']
        unit = student.objects.create(cName=cName, cSex=cSex, cBirthday=cBirthday, cEmail=cEmail,cPhone=cPhone, cAddr=cAddr) 
        unit.save()  #寫入資料庫
        students = student.objects.all().order_by('-id')  #依id遞減排序
        return render(request, "listall.html", locals())
    else:
        return render(request,"insert.html",locals())
	
def modify(request):  #修改資料
    name = request.GET['name']
    unit = student.objects.get(cName=name)
    if request.method == 'POST':
        unit.cName = request.POST['name']
        unit.cSex = request.POST['sex']
        birthday = request.POST['birthday']
        birthday = ((birthday.replace('年','-')).replace('月','-')).replace('日','')
        unit.cBirthday = birthday
        unit.cEmail = request.POST['email']
        unit.cPhone = request.POST['phone']
        unit.cAddr = request.POST['addr']
        unit.save()  #寫入資料庫
        students = student.objects.all().order_by('-id')  #依id遞減排序
        return render(request, "listall.html", locals())
    else:
        sex = unit.cSex
        birthday = unit.cBirthday
        email = unit.cEmail
        phone = unit.cPhone
        addr = unit.cAddr
        return render(request,"modify.html",locals())

def delete(request,id=None):  #刪除資料
    name = request.GET['name']
    unit = student.objects.get(cName=name)
    unit.delete()
    students = student.objects.all().order_by('-id')
    return render(request, "listall.html", locals())

def listall2(request):  
	students = student.objects.all().order_by('id')  #依id遞增排序
	return render(request, "listall2.html", locals())


