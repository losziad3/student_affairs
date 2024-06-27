from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from .models import *
import json

# Create your views here.

def index(request):
    return render(request,'pages/index.html')

def add(request):
    if request.method == "POST":
        ID = request.POST.get('id')
        Name = request.POST.get('name')
        Dept = request.POST.get('department')
        Em = request.POST.get('email')
        Lvl = request.POST.get('level')
        gpa = request.POST.get('gpa')
        Phone = request.POST.get('phone')
        Date = request.POST.get('date')
        Gender = request.POST.get('Gender')
        Status = request.POST.get('status')
        stuData = Student(studentID=ID,level=Lvl, name=Name, Email=Em, department=Dept,
                    GPA=gpa,phone=Phone, date=Date, gender=Gender, status=Status)
        stuData.save()
        return  redirect("list")
    return render(request,'pages/add.html')
def edit(request,id):
    if request.method=="POST":
        editST = Student.objects.get(studentID = id)
        editST.studentID = request.POST.get('id')
        editST.name = request.POST.get('name')
        editST.Email = request.POST.get('email')
        editST.level = request.POST.get('level')
        editST.GPA = request.POST.get('gpa')
        editST.phone = request.POST.get('phone')
        editST.department = request.POST.get('department')
        editST.date = request.POST.get('date')
        editST.gender = request.POST.get('Gender')
        editST.status = request.POST.get('status')
        editST.save()
        return  redirect("list")
    student_id = Student.objects.get(studentID=id)
    stu = {'stu': student_id}
    return render(request,'pages/edit.html' , stu)
def update(request):
    return render(request,'pages/update.html')
def delete(request):
    return render(request,'pages/delete.html')
def about(request):
    return render(request,'pages/about-us.html')
def list_student(request):
    students = {
        'stu': Student.objects.all()
    }
    return render(request ,'pages/list.html',students)


def Search(request):
    return render(request,'pages/Search.html')

def Searchajax(request):
    if request.method == "GET":
        id = request.GET.get("id")
        students =  Student.objects.filter(studentID__contains=id).values()
        if students != "":
            data = "["
            for x in students:
                data = data + json.dumps(x, cls=DjangoJSONEncoder) + ","
            index = len(data) - 1
            data =  data[:index] + "]"
            if  data== "]":
                 data= ""
            return HttpResponse(data)
        else:
            return HttpResponse("")


def delete(request,id):
        delete_student = Student.objects.get(studentID = id)
        delete_student.delete()
        return redirect("list")
