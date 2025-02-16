from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def logins(request):
    if request.method=="POST":
        teacherid=request.POST['teacher-id']
        password=request.POST['password']
        
        auth=authenticate(request,username=teacherid,password=password)
        
        if auth is not None:
           login(request,auth)

           return redirect('dashboard')

        else:
            return redirect('login')

        
    return render(request,'login.html')

def dashboard(request):
    return render(request,'dashboard.html')