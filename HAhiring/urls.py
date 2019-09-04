"""
Definition of urls for HAhiring.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
# from app.views import code


urlpatterns = [
  
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('codeeditor/',views.codeeditor, name='codeeditor'),
    path('code/',views.code, name='code'),
    path('test/code1/',views.code1, name='code1'),
    path('test/',views.test, name='test'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls, name='admin'),
]
