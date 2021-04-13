from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm, UserUpdateForm

# Create your views here.
def home(request):
    posts = Post.objects.all()
    page = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = page.get_page(page_number)  
    context = {
        'page_obj': page_obj
    }
    return render(request, 'home.html', context)

def view_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post', post_slug)
    form = CommentForm()
    context = {
        'post': post,
        'form': form
    }
    return render(request, 'post.html', context)

def view_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    posts = Post.objects.filter(author=user)
    page = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = page.get_page(page_number)  
    context = {
        'usr': user,
        'page_obj': page_obj
    }
    return render(request, 'user.html', context)

@login_required(login_url='login')
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    context = {
        'form': form,
        'title': "Create Post"
    }
    return render(request, 'create_and_edit_post.html', context)

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = UserCreationForm
    context = {
        'form': form
    }
    return render(request, 'signup.html', context)
    
@login_required(login_url='login')
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author == request.user:
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = PostForm(instance=post)
    else:
        form = None
        redirect('home')
    context = {
        'form': form,
        'title': "Edit Post"
    }
    return render(request, 'create_and_edit_post.html', context)
    
@login_required(login_url='login')
def delete_post(request):
    post_id = request.POST.get('post_id')
    post = get_object_or_404(Post, id=post_id)
    if post.author == request.user:
        post.delete()
        return redirect('home')
    else:
        return redirect('home')

@login_required(login_url='login')
def edit_user(request):
    form = UserUpdateForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'edit_user.html', context)


def search(request):
    search_query = request.GET.get('search')
    posts = Post.objects.filter(title__icontains=search_query)
    page = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = page.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'search.html', context)