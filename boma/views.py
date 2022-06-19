
from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Profile,Post,Business,NeighbourHood


# Create your views here.
def index(request):
    return render(request,"index.html")

def home(request):
    neighbourhoods = NeighbourHood.objects.all()
    print(neighbourhoods)

    context = {
        'neighbourhoods': neighbourhoods
    }
    return render(request,"home.html",context)
    

def register(request):
    form=RegisterUserForm

    if request.method =='POST':
        form= RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,("registration successful"))
        
            return redirect('login')
    context={'form':form}

    return render(request,'registration/register.html',context)

def login_in(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,("login successful"))
            return redirect('home')
        
    context={}
    return render(request,'registration/login.html')

def log_out(request):
    logout(request)
    return redirect('index')

@login_required(login_url='login')
def profile(request):
    profiles=Profile.objects.get(user=request.user)
    # hoods=NeighbourHood.objects.filter(user=request.user)
       
    context={
        
        'profiles':profiles, 
        }
    return render(request, 'profile.html',context)

@login_required(login_url='login')
def update_profile(request):
    profiles = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        prof_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if  prof_form.is_valid():
            prof_form.save()
            return redirect('profile')
       
    else:
        
        prof_form = UpdateProfileForm(instance=request.user.profile)
             
    context={
        'profiles':profiles,
      
        'prof_form': prof_form,
        
        }
    
    return render(request, 'update_profile.html',context)

# @login_required(login_url='login')
# def hoods(request):
#     neighbourhoods = NeighbourHood.objects.all()
#     print(neighbourhoods)
#     # all_hoods = all_hoods[::-1]
    
#     context = {
#         'neighbourhoods': neighbourhoods
#     }
#     return render(request, 'home.html', context)

def create_hood(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('home')
    else:
        form = NeighbourHoodForm()
    return render(request, 'create_hood.html', {'form': form})

def join_hood(request, id):
    neighbourhood=NeighbourHood.objects.get(id=id)
    request.user.profile.neighbourhood = neighbourhood
    request.user.profile.save()

    context={
            'neighbourhood' : neighbourhood,
            
            }
    return render(request,'join_hood.html',context ) 
    
