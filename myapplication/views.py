from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
import pyodbc
from .form import Customuserform
from django.contrib import messages
from django.contrib.auth import authenticate,login

def connection():
    s = 'copflidar.database.windows.net' #Your server name 
    d = 'copflidar' 
    u = 'testuser' #Your login
    p = 'bpp#12345678' #Your login password
    cstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+s+';DATABASE='+d+';UID='+u+';PWD='+ p
    conn = pyodbc.connect(cstr)
    return conn

# Create your views here.

def homepage(request):
    return render(request,"homepage.html")


def register(request):
    form=Customuserform()
    if request.method=='POST':
        form=Customuserform(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,"Registration Success")
        return redirect('/submit')

    return render(request,"register.html",{'form':form})


def login_page(request):
    if request.method=='POST':
        name=request.POST.get('username')
        pwd=request.POST.get('password')
        user=authenticate(request,username=name,password=pwd)
        if user is not None:
            login(request,user)
            messages.success(request,"Login Success")
            return redirect('/')
        else:
            messages.error(request,"Invalid Login")
            return redirect("/login")
    return render(request,"login.html")
    

# def submit_btn(request):
#     if request.headers.get('X-Requested-With')=='XMLHttpRequest':
#         data = json.load(request)
#         inpt = data['inp']
#         conn = connection()
#         cursor = conn.cursor()
#         cursor.execute("exec test123 ?", inpt)
#         conn.commit()
#         conn.close()

#         return JsonResponse({'Status':'Sucess'},status=200)
#     else:
#         return JsonResponse({'Status':'Invalid Acess'},status=200)
#     return render(request,"homepage.html")


def submit_btn(request):
    print(request.method)
    if request.method=='POST':
        inpt=request.POST.get('username')
        
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("exec test123 ?", inpt)
        conn.commit()
        conn.close()
    return render(request,"homepage.html")
