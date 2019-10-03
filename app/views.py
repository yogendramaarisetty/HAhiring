"""
Definition of views.
"""
import xlrd
import xlsxwriter
import os
import array
import time
import sys
import subprocess
import json
from datetime import datetime
from subprocess import run, PIPE
from django.template.loader import render_to_string
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpRequest
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import codeForm
from subprocess import Popen,PIPE,STDOUT
from xlrd import open_workbook
from xlutils.copy import copy  
import openpyxl as op


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )


def submittest(request):

    return render(request,'app/index.html',{

    })
def set_question(request):
    question="app/"
    question+=request.POST.get("question","")
    question+=".html"
    qhtml=render_to_string(question)
    return HttpResponse(qhtml)
    
def test(request):
    return render(request,'app/basic.html',{

    })

def code1(request):
 
    rd={}
    codet=request.POST.get("code","") #taking POST code
    # q_id=request.POST.get("question_id","")
    q_id=1
    lang=request.POST.get("language_id","")
    inputraw=request.POST.get("input","") # taking POST Input
    print(lang," ",inputraw)
    if request.POST.get("submit","")=="yes":
        res={}
        print("#########\n",q_id,"\n#######")
        q_id=request.POST.get("question_id","")
        res=submit_code(codet,request.user,q_id,lang)
        return HttpResponse(json.dumps(res), content_type="application/json")
    
    # print("input is :",inputraw)

    output=execute(codet,inputraw,q_id,lang) #storing out put value of successfully executed code
    rd['result']="successfull"
    rd['msg']=output
    # print('recieved code is \n"',codet,'\n and output is\n',output)
    return HttpResponse(json.dumps(rd), content_type="application/json")#sending json response

def execute(code_text,input,q_id,lang):
    language={"Java" : "Main.java","C" : "main.c","C++" :"main.cpp"}
    print("&&&&&&&",lang)
    filename_code=open(language[lang],'w+') #creating Main.java file
    
    
    filename_code.flush() #flushing file
    f1 = code_text.split("\n") #splitting code
    for i in f1:
        filename_code.write(i+"\n")  #writing code line by line into file
    filename_code.close() #closing java file
    # time.sleea(filename_code,input) 
    return(execute_java(filename_code,input,q_id,lang))

def execute_java(java_file, input1,q_id,lang):
    s=""
    language_compile={"Java" : "javac Main.java","C" : "gcc main.c","C++" :"g++ main.cpp"}
    language_run={"Java" : "java Main","C" : "a","C++" :"a"}
    temp=subprocess.Popen(language_compile[lang],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    var=temp.stderr.readlines()
    if len(var)==0:
         p=run(language_run[lang], stdout=PIPE,input=input1, encoding='ascii')
         print(p.stdout)
         return p.stdout
    else:
        for i in var:
            s+=i.decode("utf-8")
        print(s)
        return s

def submit_code(code,user,q_id,lang):
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    s=""
    file=open("final_code.txt","w")
    file.write(code)
    arr={}
    print("Submit Code ",lang)
    print("___________________________________")
    for k in range(1,5):
        i_n=q_id+"\input "+str(k)+".txt"
        o_n=q_id+"\output "+str(k)+".txt"
        # i_f=open(i_n,"r")
        i_f=open(os.path.join(fileDir, i_n))
      
        o_f=open(os.path.join(fileDir, o_n))
       
        arr['testcase'+str(k)]=checkstatus(code,i_f,o_f,q_id,lang)
        print("***************************\n",k," = ",arr['testcase'+str(k)])
    score=0
 
    workbookpro = open_workbook('results.xls')
    workbook=copy(workbookpro)
    ques={"q1":1,"q2":2,"q3":3,"q4":4,"q5":5}
    worksheet = workbook.get_sheet(0)
    worksheet.write(1,1, str(user))
    for i in arr:
        print(arr[i])
        if arr[i] is True:
            print("@@@@@ TRUE @@@@")
            score += 10
    
    q_cell= ques[q_id]
    score_cell= ques[q_id]  
    worksheet.write(q_cell,2, q_id)
    worksheet.write(score_cell,2, score)
    
    return arr        

def  checkstatus(code,inputfile,outputfile,q_id,lang):
    i_s=""
    print("FILE ",inputfile)
    for i in inputfile.readlines():   #line by line
            i_s+=i
            # print("input= ",i_s)
    str1=execute(code,i_s,q_id,lang)
  
    str2=""
    for i in outputfile.readlines():   #line by line
            str2+=i
    
    stro=str1.replace(str2,"")
    print("diff=",stro,str1==str2)
    print("str1= ",str1,"str2= ",str2,"***",str1==str2)
    # print(str1==str2)
    return str1==str2

    
    








def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
