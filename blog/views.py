from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator
from .models import Blog, Comment, Tag
from .forms import BlogForm
from django.views.decorators.http import require_POST

def home(request):
    blogs = Blog.objects.all().order_by('-id')
    paginator = Paginator(blogs, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'home.html',{'page_obj':page_obj})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    comment = Comment.objects.filter(blog = blog)
    tag = blog.tags.all()
    return render(request,'detail.html',{'blog':blog, 'comment':comment, 'tags':tag})
    
def new(request):
    tags = Tag.objects.all()
    return render(request,'new.html', {'tags': tags})

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST.get('title')
    new_blog.content = request.POST.get('content')
    new_blog.image = request.FILES.get('image')
    new_blog.author = request.user
    new_blog.save()

    tags = request.POST.getlist('tags')
    for tag_id in tags:
        tag = Tag.objects.get(id=tag_id)
        new_blog.tags.add(tag)   

    return redirect('detail', new_blog.id)

def edit(request, blog_id):
    edit_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'edit.html', {'edit_blog':edit_blog})


def update(request, blog_id):

    old_blog = get_object_or_404(Blog, pk=blog_id)
    old_blog.title = request.POST.get('title')
    old_blog.content = request.POST.get('content')
    old_blog.image = request.FILES.get('image')
    old_blog.save()

    return redirect('detail', old_blog.id)

    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.save()
        return redirect('detail', old_blog.id)

    return render(request, 'new.html', {'old_blog':old_blog})


def delete(request, blog_id):
    delete_blog = get_object_or_404(Blog, pk=blog_id)
    delete_blog.delete()
    return redirect('home')

def create_comment(request, blog_id):
    comment = Comment()
    comment.content = request.POST.get('content')
    comment.author = request.user
    comment.save()
    return redirect('detail', 'blog_id')

def new_comment(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'new_comment.html', {'blog':blog})
    
import logging

logger = logging.getLogger(__name__)

def likes(request, blog_pk):
    if request.user.is_authenticated:
        logger.debug(f"Authenticated user: {request.user.pk}")
        blog = get_object_or_404(Blog, pk=blog_pk)
        if blog.like_users.filter(pk=request.user.pk).exists():
            blog.like_users.remove(request.user)
            logger.debug("Like removed.")
        else:
            blog.like_users.add(request.user)
            logger.debug("Like added.")
        return redirect('detail', blog_id=blog.pk)
    else:
        logger.debug("User not authenticated.")
    return redirect('accounts:login')
