from django.shortcuts import render, redirect
from .models import Post, Comment

# Create your views here.

def forum(request):

    posts = Post.objects.all().order_by('-created_date')
    return render(request,'forum/forum.html',context={'posts':posts})

def make_post(request):

    username = request.user.username
    title = request.POST['title']
    text = request.POST['content']

    # Creating a post instance
    post = Post(author=username, title=title, text=text)
    post.save()
    return redirect('/')

def view_post(request,pk):

    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)

    return render(request, 'forum/thread.html',context={'comments':comments,'post':post})


def make_comment(request,pk):

    username = request.user.username
    text = request.POST['content']

    # Creating a post instance
    comment = Comment(post=Post.objects.get(pk=pk), author=username, text=text)
    comment.save()
    return redirect('/posts/' + str(pk))
