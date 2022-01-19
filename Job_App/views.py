from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User 

# Create your views here.

def index(request):
    return render(request, 'index.html')

def admin_login(request):
    return render(request, 'admin_login.html')

def user_login(request):
    return render(request, 'user_login.html')
    
def recruiter_login(request):
    return render(request, 'recruiter_login.html')

def user_signup(request):
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        con = request.POST['contact']
        e = request.POST['email']
        p = request.POST['pwd']
        try:
            user = User.objects.create_user(first_name=f, last_name=l, username=e, password=p)
            StudentUser.objects.create(user=user,mobile=con,type="Student")
            error="no"
            
        except:
            error="yes"
    d = {'error':error}
    return render(request, 'user_signup.html', d)
    