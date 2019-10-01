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
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpRequest
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import codeForm
from subprocess import Popen,PIPE,STDOUT



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
        res=submit_code(codet,request.user)
        return HttpResponse(json.dumps(res), content_type="application/json")
    
    # print("input is :",inputraw)

    output=execute(codet,inputraw,q_id,lang) #storing out put value of successfully executed code
    rd['result']="successfull"
    rd['msg']=output
    # print('recieved code is \n"',codet,'\n and output is\n',output)
    return HttpResponse(json.dumps(rd), content_type="application/json")#sending json response

def execute(code_text,input,q_id,lang):
    language={"Java" : "Main.java","C" : "main.c","C++" :"main.cpp"}
    
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


    # try:
    #     subprocess.check_output('javac Main.java', shell=True) #compiling and checking compile output 
    #                                                            #Note: check_output command returns exceptionif compilation fails
    # except:
    #     subprocess.Popen('javac Main.java 2> errorlog.txt', shell=True) #logging errorcommand
    #     time.sleep(2) #sleep 
    #     f=open('errorlog.txt','r')  #writing compilation error to log file
    #     for i in f.readlines():   #line by line
    #         s+=i
        
    #     # print("#####\n",s,"\n#####")
    #     return s
    # cmd =[ 'java ', 'Main']
    # p = run(cmd, stdout=PIPE,input=input1, encoding='ascii') #passing input to run command
    # print(p.stdout)
    # return p.stdout
    
def submit_code(code,user):
    s=""
    file=open("final_code.txt","w")
    file.write(code)
    arr={}
    
    for k in range(1,5):
        i_n="input "+str(k)+".txt"
        o_n="output "+str(k)+".txt"
        i_f=open(i_n,"r")
        o_f=open(o_n,"r")
        arr['testcase'+str(k)]=checkstatus(code,i_f,o_f)
        print("***************************\n",k," = ",arr['testcase'+str(k)])
    score=0
    for i in arr:
        print(arr[i])
        if arr[i] is True:
            print("@@@@@ TRUE @@@@")
            score += 10
    workbook = xlsxwriter.Workbook('results.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', str(user))
    worksheet.write('B1', str(score))
    workbook.close()
    return arr        

def  checkstatus(code,inputfile,outputfile):
    i_s=""
    for i in inputfile.readlines():   #line by line
            i_s+=i+'\n'
    print("input= ",i_s)
    str1=execute(code,i_s)
  
    str2=""
    for i in outputfile.readlines():   #line by line
            str2+=i+'\n'
    
    
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
