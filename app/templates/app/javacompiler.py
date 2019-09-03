import os
import requests
# os.environ.set("PATH=C:/Program Files (x86)/Java/jdk1.8.0_181/bin")
# print(os.environ)
cc="javac"
out="java Main"
code=requests.post["code"] 
input=$_POST["input"] 
filename_code="Main.java" 
filename_in="input.txt" 
filename_error="error.txt" 
runtime_file="runtime.txt" 
executable="*.class" 
command=$CC." ".$filename_code 
command_error=$command." 2>".$filename_error 
runtime_error_command=$out." 2>".$runtime_file