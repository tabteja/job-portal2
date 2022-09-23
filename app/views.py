from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from app.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import random
from django.utils.decorators import method_decorator
from django.http.response import HttpResponse
from app.models import *
from django.db.models import F

# Create your views here.


def indexview(request):
    if not request.user.is_authenticated:
        return render(request,'index.html')
    else:
        return redirect('dashboard')
    
    
def dashboard(request):
    if not request.user.is_authenticated:
        return render(request,'index.html')
    else:
        return render(request,'dashboard.html')


def jobs(request):
    j = Job.objects.all()
    return render(request,'jobs.html',{'j':j})
    
    
def search(request):
    query = request.GET.get('query')
    j = Job.objects.filter(title__icontains = query)
    return render(request,'search.html',{'j' : j})


def companies(request):
    return render(request,'companies.html')


def services(request):
    return render(request,'services.html')


def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')


@login_required(login_url='login')
def resume(request):
    if request.method == "POST":  
        form = ResumeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('show')  
            except:  
                pass  
    else:  
        form = ResumeForm()  
    return render(request,'index.html',{'form':form})  


@login_required(login_url='login')
def show(request):  
    resumes = Resume.objects.all()  
    return render(request,"show.html",{'resumes':resumes}) 


@login_required(login_url='login')
def edit(request, id):  
    resume = Resume.objects.get(id=id)  
    return render(request,'edit.html', {'resume':resume}) 


@login_required(login_url='login')
def update(request, id):  
    resume = Resume.objects.get(id=id)  
    form = ResumeForm(request.POST, instance = resume)  
    if form.is_valid():  
        form.save()  
        return redirect('show')  
    return render(request, 'edit.html', {'resume': resume})  


@login_required(login_url='login')
def destroy(request, id):  
    resume = Resume.objects.get(id=id)  
    resume.delete()  
    return redirect('show')  


@login_required(login_url='login')
def profile(request):
    return render(request,'profile.html')


@login_required(login_url='login')
def profile_edit(request):
    return render(request,'profile_edit.html')


@login_required(login_url='login')
def profile_update(request):
    return render(request,'profile_update.html')


@login_required(login_url='login')
def employee(request):
    return render(request,'employee.html')


@login_required(login_url='login')
def post_a_job(request):
    return render(request,'post_a_job.html')


@login_required(login_url='login')
def show_job(request):
    return render(request,'show_job.html')


@login_required(login_url='login')
def edit_job(request):
    return render(request,'edit_job.html')


@login_required(login_url='login')
def update_job(request):
    return render(request,'update_job.html')


@login_required(login_url='login')
def delete_job(request):
    return render(request,'delete_job.html')


def loginview(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user1=authenticate(username=username,password=password)
            if user1 is not None:
                login(request,user1)
                return redirect('dashboard')
        return render(request,'login.html')
    else:
        return redirect('dashboard')


def logoutview(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')


def registerview(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            user = User.objects.create_user(username,email,password)
            user.save()
            messages.success(request,'Thanks for signup..! please login')
            return redirect('login')
        return render(request,'register.html')
    else:
        return redirect('dashboard')