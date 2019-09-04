"""
Definition of views.
"""
import os
import subprocess
from datetime import datetime

from django.core.serializers import json
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
    if request.method == 'POST' :
        codet=request.POST.get("code","")
        print(code(codet))
        response_data={}
        try:
            response_data['result']="Successful"
            response_data['message']=code
        except:
            response_data['result']="Oh no"
            response_data['message']="didnt run"
        print('recieved code is \n"',codet,'"')
    return render(request,'app/index.html',{

    })

def code(code_text):
    return execute(code_text)

# def code(request):
#         code_text=""
#         output = ""
#         # form = (request.POST)
#         if request.method=='POST':
#             code_text = request.POST['codetext']
#             print(code_text)
#             output =  execute(code_text)
#
#
#         form  = codeForm
#         return render(request,'app/basic.html',{
#             'form': codeForm,
#             'codetext': code_text,
#             'output': output,}
#         )
def compile_java(java_file):
   proc = subprocess.Popen('javac Main.java', shell=True)

def execute_java(java_file, stdin):
    #java_class,ext = os.path.splitext(java_file)
    cmd = ['java ', 'Main']
    proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    stdout,stderr = proc.communicate(stdin)
    stdoutstr= str(stdout,'utf-8')
    return stdoutstr

def execute(code_text):
    cc="javac"
    out="java Main"

    input=""
    filename_code=open('Main.java','w') #creating file
    f1 = code_text.split("\n")
    for i in f1:
        filename_code.write(i+"\n")
    compile_java(filename_code)
    return execute_java(filename_code,input)


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
