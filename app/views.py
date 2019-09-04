"""
Definition of views.
"""
import os
import subprocess
from datetime import datetime
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


def code(request):
        code_text=""
        output = ""


        if request.method=='POST':
            form = codeForm(request.POST)
            if form.is_valid():

                code_text = form.cleaned_data['body']

                output =  execute(code_text)
        form  = codeForm
        return render(request,'app/basic.html',{
            'form':form,


        }
        )
def compile_java(java_file):
   proc = subprocess.Popen('javac Main.java', shell=True)

def execute_java(java_file, stdin):
    #java_class,ext = os.path.splitext(java_file)
    cmd = ['java ', 'Main']
    proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    stdout,stderr = proc.communicate(stdin)
    return str(stdout)

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
    # filename_in=open('user_input.txt','r+')
    # filename_error=('error.txt','r+')
    # runtime_file=('runtime.txt','r+')
    # executable=('*.class','r+')


    # command=$CC." ".$filename_code
    # command_error=$command." 2>".$filename_error
    # runtime_error_command=$out." 2>".$runtime_file


# def admin(request):
#     assert isinstance(request,HttpRequest)
#     return(request,'env/Lib/site-packages/django/contrib/admin/sites.py',
#         {
#         'title':'Admin Management',
#         'message': 'your management page',

#         }

#     )

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
