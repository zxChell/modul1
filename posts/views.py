from django.shortcuts import render, redirect
from .froms import *
from .models import *


def index(request):
    post = Post.objects.all()
    return render(request, 'posts/index.html', context={'post': post})


def create(request):
    create_category()

    if request.method == 'POST':

        form = AddPost(request.POST)
        if form.is_valid():

            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            category = form.cleaned_data['category']

            Post.objects.create(title=title, content=content, category=category)
            return redirect('home')
        else:
            form = AddPost()
            return render(request, 'posts/create.html', context={'form': form})
    else:
        form = AddPost()
        return render(request, 'posts/create.html', context={'form': form})


def delete(request, id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
        return redirect('home')
    except:
        return redirect('home')


def update(request, id):
    try:
        post = Post.objects.get(id=id)
        if request.method == 'POST':
            post.title = request.POST.get('title')
            post.content = request.POST.get('content')
            post.save()
            return redirect('home')
        else:
            return render(request, 'posts/update.html', context={'post': post})
    except:
        return redirect('create')


def post(request, id):
    try:
        post = Post.objects.get(id=id)
        return render(request, 'posts/post.html', context={'post': post})
    except:
        return redirect('home')


def create_category():
    if Category.objects.all().count() == 0:
        Category.objects.create(name='sport')
        Category.objects.create(name='beauty')
        Category.objects.create(name='health')
