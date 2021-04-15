from django.shortcuts import redirect, render
from .forms import SignUpForm, LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Post
from django.contrib.auth.models import Group, User
# Create your views here.

#Home
def Home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts':posts})

#About
def About(request):
    return render(request, 'blog/about.html')

#Contact
def Contact(request):
    return render(request, 'blog/contact.html')

#Dashboard
def Dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        fullname = user.get_full_name()
        gps = user.groups.all()
        return render(request, 'blog/dashboard.html', {'posts':posts, 'name':fullname,'groups':gps})
    else:
        messages.warning(request, 'You are not logged in. Please login')
        return redirect('login')

#Login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password= upass)
                if user is not None:
                    login(request,user)
                    messages.success(request, 'You have logged in successfully')
                    return redirect('dashboard')
        else:
            fm = LoginForm()
        return render(request, 'blog/login.html', {'form':fm})
    else:
        return redirect('dashboard')

#SignUp
def user_signup(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            user = fm.save()
            group = Group.objects.get(name='author')
            user.groups.add(group)
            messages.success(request, 'You have register successfully !!!')
            return redirect('login')
    else:
        fm = SignUpForm()
    return render(request, 'blog/signup.html', {'form':fm})

#Logout
def user_logout(request):
    logout(request)
    return redirect('home')

#Add Post

def add_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PostForm(request.POST)
            if fm.is_valid():
                title = fm.cleaned_data['title']
                desc = fm.cleaned_data['desc']
                pst = Post(title=title, desc=desc)
                pst.save()
                messages.success(request, 'Post added successfully !!!')
                return redirect('dashboard')
        else:
            fm = PostForm()
        return render(request, 'blog/addpost.html', {'form':fm})
    else:
        return redirect('login')
def edit_post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Post.objects.get(pk=id)
            fm = PostForm(request.POST, instance=pi)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Post edited successfully !!!')
                
        else:
            pi = Post.objects.get(pk=id)
            fm = PostForm(instance=pi)
        return render(request, 'blog/editpost.html', {'form':fm})
    else:
        return redirect('login')

def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Post.objects.get(pk=id)
            pi.delete()
            return redirect('dashboard')
    else:
        return redirect('login')

#user profile
def user_profile(request):
    user = User.objects.get(username = request.user.username)
    return render(request, 'blog/profile.html',{'userdetails':user})