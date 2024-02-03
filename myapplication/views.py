from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
import pyodbc
import pandas as pd
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.views.decorators.csrf import csrf_exempt
from .form import Customuserform,ApplyLeave
from django.contrib.auth.forms import AuthenticationForm #add this
from django.db import IntegrityError


def connection():
    s = 'copflidar.database.windows.net' #Your server name 
    d = 'copflidar' 
    u = 'testuser' #Your login
    p = 'bpp#12345678' #Your login password
    cstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+s+';DATABASE='+d+';UID='+u+';PWD='+ p
    conn = pyodbc.connect(cstr)
    return conn

# Create your views here.
@csrf_exempt
def homepage(request):
    return render(request,"homepage.html")

@csrf_exempt
def register(request):
    form=Customuserform()
    if request.method=='POST':
        form=Customuserform(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,"Registration Success")
        return redirect('/submit')

    return render(request,"register.html",{'form':form})

@csrf_exempt
def login_page(request):
    if request.method=='POST':
        name=request.POST.get('username')
        pwd=request.POST.get('password')
        user=authenticate(request,username=name,password=pwd)
        if user is not None:
            login(request,user)
            messages.success(request,"Login Success")
            return redirect('/submit')
        else:
            messages.error(request,"Invalid Login")
            return redirect("/login")
    
    form = AuthenticationForm()
    return render(request,"login.html",context={"login_form":form})
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

@csrf_exempt
def submit_btn(request):
    
    conn = connection()
    cursor = conn.cursor()
    if request.method=='POST':
        inpt=request.POST.get('selected_date')
        inpt1=request.POST.get('wfhdate')
        print(type(inpt),inpt.split(', '))
        # cursor.execute("exec test123 ?", inpt)
        # conn.commit()
        try:
            cursor.execute(f"exec test1234 ?", inpt1)
            rows = cursor.fetchall()
            column_names = [column[0] for column in cursor.description]
            df = pd.DataFrame([tuple(row) for row in rows], columns=column_names)

            # Print or use the DataFrame as needed
            if 'Error' in column_names:
                for error_tup in rows:
                    for error in error_tup:
                        messages.error(request,error)
            else:
                df = df
        except pyodbc.Error   as e:
            # Capture the specific SQL error (IntegrityError in this case)
            print(e)
            messages.error(request,'Please Contact Admin')


    leaveform = ApplyLeave()
    dataset = dict()
    dataset['leaveform'] = leaveform 
    queryset = cursor.execute("select flidarid,flidarname,installationdate from flidardet")
    df_out =  queryset.fetchall()
    conn.close()
    leavedt = ["10-1-2024","12-1-2024"]
    events = [{'title': 'All Day Event','start': '2024-02-02'},{'title': 'Long Event','start': '2024-02-03', 'color': 'red'}]
    events_json = json.dumps(events)

    return render(request,"homepage.html",context={"leaveform":leaveform , 'data':df_out , 'leave_dt':leavedt, 'events':JsonResponse(events, safe=False)} )

from datetime import date
@csrf_exempt
def dashboard(request):
    
    event_list = []

    
    event_list.append({
        'title': 'Test',
        'start': date.today().isoformat(),
        'end': date.today().isoformat() if date.today() else None,
    })

    # return JsonResponse(event_list, safe=False)
    return render(request,'dashboard.html')