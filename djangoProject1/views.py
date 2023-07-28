import msilib.schema

from django.shortcuts import render
from django.http import HttpResponse
from math import ceil

import student.models
from student.models import student
from student.models import fees


def index(request):
    return render(request, 'index.html')


def new_stu(request):
    return render(request, 'new_stu.html')


def add_stu(request):
    student_name = request.POST.get("student_name")
    father_name = request.POST.get("father_name")
    Address = request.POST.get("Address")
    City = request.POST.get("City")
    Age = request.POST.get("Age")
    Class = request.POST.get("Class")
    Mobile_no = request.POST.get("Mobile_no")
    Gender = request.POST.get("Gender")
    l= fees.objects.get(Class=Class)
    fees2=l.fees
    d_f=fees2
    data = student(student_name=student_name, Father_name=father_name, Address=Address, City=City, Age=Age, Class=Class,
                   Mobile_no=Mobile_no, Gender=Gender, due_fees=d_f)
    data.save()
    return render(request, 'index.html')


def stu_info(request):
    stu_list = student.objects.all()
    return render(request, 'stu_info.html', {'stu_list': stu_list})


def back(request):
    return render(request, 'index.html')


def update_info(request):
    return render(request, 'update_info.html')


def check_stu(request):
    name = request.POST.get("name")
    s = student.objects.get(student_name=name)
    return render(request, 'stuinfo.html', {'s': s})

def submit(request):
    addr = request.POST.get("addr")
    city = request.POST.get("city")
    age = request.POST.get("age")
    class1 = request.POST.get("class")
    mob = request.POST.get("mobile")
    gender = request.POST.get("gender")
    name = request.POST.get("name")
    s = student.objects.get(student_name=name)
    s.Address = addr
    s.City = city
    s.Age = age
    s.Class = class1
    s.Mobile_no = mob
    s.Gender = gender
    s.save()
    return render(request, 'index.html')

def fee_update(request):
    c = fees.objects.all()
    return render(request, 'fee_update.html', {'c': c})

def fees1(request, id):
    fees2 = request.POST.get(str(id))
    m = fees.objects.get(Class = id)
    m.fees = fees2
    m.save()
    c = fees.objects.all()
    return render(request, 'fee_update.html', {'c': c})


def fee_detail(request):
    data = fees.objects.all()
    return render(request, 'fee_detail.html', {'data': data})

def fee_info(request):
    return render(request, 'fee_info.html')


def stu_fees(request):
    name = request.POST.get("name")
    Class4 = request.POST.get("Class3")
    m = student.objects.get(student_name=name, Class=Class4)
    return render(request, 'fee_info2.html', {'m': m})


def info(request, id):
    paid_fees= request.POST.get("paid_fees")
    m = student.objects.get(id = id)
    k = m.Class
    paid = int(paid_fees)
    h = fees.objects.get(Class=k)
    fee5= m.due_fees
    d_f = fee5 - paid
    m.due_fees = d_f
    m.paid_fees = m.paid_fees + paid
    m.save()
    return render(request, 'fee_info2.html', {'m': m})



def scho_info(request):
    return render(request, 'scho_info.html')