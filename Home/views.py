from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group
from .forms import UserAddform
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .decorators import admin_only
from Events.models import EventModel

@admin_only
def EventHome(request):
    events = EventModel.objects.all()
    context = {
        "events":events
    }
    return render(request,'index.html',context)

def SignIn(request):
    if request.method  == 'POST':
        username = request.POST['uname']
        password = request.POST['pswd']
        user1 = authenticate(request, username = username , password = password)
        
        if user1 is not None:
            request.session['username'] = username
            request.session['password'] = password
            login(request, user1)
            return redirect('EventHome')
        
        else:
            messages.info(request,'Username or Password Incorrect')
            return redirect('SignIn')
    
    return render(request,"login.html")

def SignUp(request):
    form = UserAddform()
    if request.method == 'POST':
        form = UserAddform(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username  = form.cleaned_data.get('username')
            
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username Already exists")
                return redirect('registration')
            
            elif User.objects.filter(email = email).exists():
                messages.info(request,"Email Already taken")
                return redirect('registration')
            
            else:
                new_user = form.save()
                new_user.save()
                messages.success(request,"Your Account Created Successfully")
                return redirect('SignIn')
    context = {
        "form":form
    }
    return render(request,"register.html",context)

def EventGroupSignUp(request):
    form = UserAddform()
    if request.method == 'POST':
        form = UserAddform(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username  = form.cleaned_data.get('username')
            
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username Already exists")
                return redirect('registration')
            
            elif User.objects.filter(email = email).exists():
                messages.info(request,"Email Already taken")
                return redirect('registration')
            
            else:
                new_user = form.save()
                new_user.save()
                group = Group.objects.get(name="eventgroup")
                new_user.groups.add(group)
                
                messages.success(request,"Your Account Created Successfully")
                return redirect('SignIn')
            
    context = {
        "form":form
    }
    return render(request,"Register_EventGroups.html",context)

def SignOut(request):
    logout(request)
    return redirect("EventHome")