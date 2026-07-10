from django.shortcuts import redirect, render
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def home(request):
    posts = Post.objects.all()
    context = {
        "site_name": "My Blog",
        "posts": posts,
    }
    return render(request, 'home.html', context)

def about(request):
    context ={
        'title': 'About Us',
    }

    return render(request, 'about.html', context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'post_detail.html', context)

def user_posts(request, username):
    posts=Post.objects.filter(author__username=username)
    context = {'posts': posts, 'username': username}
    return render(request, 'user_posts.html', context)

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # Include request.FILES to handle file uploads
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Assign the current user as the author
            post.save()
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'create_post.html', context)

@login_required
def edit_post(request, post_id):
    post = Post.objects.get(id=post_id, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
    else:
        form = PostForm(instance=post)
    context = {'form': form}
    return render(request, 'create_post.html', context)

@login_required
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id, author=request.user)
    post.delete()
    return redirect('/')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

