"""
Definition of views.
"""
import os
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
from .models import Post
def posts(request):
    posts = Post.objects.all()  # Getting all the posts from database
    return render(request, 'app/basic.html', { 'posts': posts })

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
def codeeditor(request):
     return render(
        request,
        'app/codeeditor.html',
        {
            'title':'Code Editor',
            'year':datetime.now().year,
        }
    )


def test(request):
    return render(request,'app/basic.html',{

    })
def code1(request):
    print ('\n******this is code1********\n')
   
    rd={}
    codet=request.POST.get("code","")
    inputraw=request.POST.get("input","") # recieved code
    
    print("input is :",inputraw)

    output=execute(codet,inputraw) #storing out put value of successfully executed code
    rd['result']="successfull"
    rd['msg']=output
    print('recieved code is \n"',codet,'\n and output is\n',output)
    return HttpResponse(json.dumps(rd), content_type="application/json")#sending json response

def execute(code_text,input):

    filename_code=open('Main.java','w+') #creating Main.java file
    filename_code.flush() #flushing file
    f1 = code_text.split("\n") #splitting code
    for i in f1:
        filename_code.write(i)  #writing code line by line into file
    filename_code.close() #closing java file
    # time.sleep(0.05)                 #waiting to get the file ready
    # execute_java(filename_code,input) 
    return(execute_java(filename_code,input))

def execute_java(java_file, input1):
    s=""
    try:
        subprocess.check_output('javac Main.java', shell=True) #compiling and checking compile output
    except:
        
        subprocess.Popen('javac Main.java 2> errorlog.txt', shell=True) #logging errorcommand
        time.sleep(2) #sleep 
        f=open('errorlog.txt','r')  #writing compilation error to log file
        for i in f.readlines():   #line by line
            s+=i
        
        # print("#####\n",s,"\n#####")
        return s
    cmd = ['java ', 'Main']
    if input == "":                                             #cheching weather input is emptyu or not
       proc = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
       stdout,stderr = proc.communicate()
       stdoutstr= str(stdout,'utf-8')
       return stdoutstr
    else :
        print("%%%%%===",input1)
        p = run(cmd, stdout=PIPE,input=input1, encoding='ascii') #taking input
        print(p.stdout)
        return p.stdout
    
   
    








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
