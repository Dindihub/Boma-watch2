
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
    posts=Post.objects.filter(hood=neighbourhood)
    business=Business.objects.filter(neighbourhood=neighbourhood)
    request.user.profile.neighbourhood = neighbourhood
    request.user.profile.save()

    context={
            'neighbourhood' : neighbourhood,
            'posts':posts,
            'business':business,
            
            }
    return render(request,'join_hood.html',context )

# @login_required(login_url='login')
# def update_hood(request):
#     neighbourHood = NeighbourHood.objects.get(user=request.profile.user)

#     if request.method == 'POST':
#         hood_form = UpdateHoodForm(request.POST, request.FILES, instance=request.user.profile)
#         if  hood_form.is_valid():
#             hood_form.save()
#             return redirect('join_hood')
       
#     else:
        
#         hood_form = UpdateHoodForm(instance=request.user.profile)
             
#     context={
#         'neighbourhood':neighbourHood,
      
#         'hood_form': hood_form,
        
#         }
    
#     return render(request, 'update_hood.html',context)
 
@login_required(login_url='login')
def create_post(request, hood_id):
    hood = NeighbourHood.objects.get(id=hood_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood = hood
            post.user = request.user.profile
            post.save()
            return redirect('join_hood', hood.id)
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})

@login_required(login_url='login')
def add_business(request, hood_id):
    hood = NeighbourHood.objects.get(id=hood_id)
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            business = form.save(commit=False)
            business.hood = hood
            business.user = request.user.profile
            business.save()
            return redirect('join_hood', hood.id)
    else:
        form = BusinessForm()
    return render(request, 'addbusiness.html', {'form': form})

def search_business(request):
    if 'business' in request.GET and request.GET["business"]:
    # if request.method == 'GET':
        search_term= request.GET.get("business")
        results = Business.search_business(search_term)
        print(results)
        message = f'search_term'
        context = {
            'results': results,
            'message': message
        }
        return render(request, 'search.html', context)
    else:
        message = "You haven't searched for any image category"
    return render(request, 'search.html', {'message': message})












    
