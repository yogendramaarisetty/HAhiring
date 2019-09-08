"""
Definition of views.
"""
import os
import time
import sys
import subprocess
import json
from datetime import datetime
# from django.utils import simplejson
# from django.core.serializers import json
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

# def compiler(request):
#      return render(
#         request,
#         'app/basic.html',
#         {
#             'title':'compiler',
#             'year':datetime.now().year,
#         }
#     )
def test(request):
    return render(request,'app/basic.html',{

    })
def code1(request):
    print ('\n******this is code1********\n')
    response_data={}
    rd={}
    codet=request.POST.get("code","") # recieved code
    code(codet)      # Calling execute function
    output=code(codet) #storing out put value of successfully executed code
    response_data['result']="Successfull"
    response_data['message']=code(codet)
    rd['msg']=response_data['message']
    rd['msg']=output
    print('recieved code is \n"',codet,'"\n and output is')
    print(output)
    return HttpResponse(json.dumps(rd), content_type="application/json")#sending json response

def code(code_text):
    return execute(code_text)

def execute(code_text):
    input=""
    filename_code=open('Main.java','w+') #creating file
    filename_code.flush()
    f1 = code_text.split("\n")
    for i in f1:
        filename_code.write(i+"\n")
    filename_code.close()
    time.sleep(0.5)
    execute_java(filename_code,input)
    return(execute_java(filename_code,input))

def execute_java(java_file, stdin):
    s="ERROR"
    try:
        subprocess.check_output('javac Main.java', shell=True)
    except:
        p= subprocess.Popen('javac Main.java', shell=True)
        errlog=open('errorlog.txt','w+')
        try:
            subprocess.check_output('javac Main.java 2> errorlog.txt', shell=True)
        except:
            with open('errorlog.txt', 'r') as file:
                data = file.read().replace('\n', '')
            print("#####\n",data,"\n#####")
            return data
    proc = subprocess.Popen('javac Main.java', shell=True) #compiling my file
    print("##################\n",proc.communicate(),"\n########################")


    cmd = ['java ', 'Main']
    proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    stdout,stderr = proc.communicate(stdin)
    stdoutstr= str(stdout,'utf-8')
    
    logfile = open('logfile.txt', 'w')
 
    proc1=subprocess.Popen(['java ', 'Main'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print("output file")
    for line in proc1.stdout:
        print(line)
        sys.stdout.write(str(line,'utf-8'))
        logfile.write(str(line,'utf-8'))
    proc1.wait()
    return stdoutstr








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
