"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpRequest
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import codeForm


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

def compiler(request):
     return render(
        request,
        'app/basic.html',
        {
            'title':'compiler',
            'year':datetime.now().year,
        }
    )

def post(request):
    form    
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
