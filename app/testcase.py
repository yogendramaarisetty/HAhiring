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