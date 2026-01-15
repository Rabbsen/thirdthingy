from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, "home.html")

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("home")
    else:
        form = PostForm()
    return render(request, "create_post.html", {"form": form})