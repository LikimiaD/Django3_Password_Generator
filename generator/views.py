from django.shortcuts import render
import random
import string

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    
    checklist = string.ascii_lowercase
    pass_ = ''
    if request.GET.get('uppercase'):
        checklist += string.ascii_uppercase
    if request.GET.get('numbers'):
        checklist += string.digits
    if request.GET.get('special'):
        checklist += string.punctuation
    
    for _ in  range(int(request.GET.get("length", 12))):
        pass_ += random.choice(checklist)
    
    return render(request, 'generator/password.html', {"password" : pass_})