from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    posts = Post.objects.all().order_by("-created_at")

    # Om någon skickar formuläret (POST)
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("/login/")

        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("home")
    else:
        form = PostForm()

    return render(request, "home.html", {"posts": posts, "form": form})

# User registration

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

# user post delete view

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Post

@login_required(login_url='/login/')
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk, user=request.user)

    if request.method == "POST":
        post.delete()  
        return redirect("home")  



