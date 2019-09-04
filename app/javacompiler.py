# import os
import requests
from .forms import codeForm
from .views import co

# from app.views import coder

# os.environ.set("PATH=C:/Program Files (x86)/Java/jdk1.8.0_181/bin")
# print(os.environ)

def code(request):
        form=""
        if request.method=='POST':
            form = codeForm(request.POST)
            if form.is_valid():

                code_text = form.cleaned_data['body']
                print('this is java comp',code_text)
        form=codeForm

print('hi')
cc="javac"
out="java Main"

# input=$_POST["input"]
# filename_code="Main.java"
# filename_in="input.txt"
# filename_error="error.txt"
# runtime_file="runtime.txt"
# executable="*.class"
# command=$CC." ".$filename_code
# command_error=$command." 2>".$filename_error
# runtime_error_command=$out." 2>".$runtime_file
