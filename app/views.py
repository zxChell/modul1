from django.shortcuts import render, redirect
from .models import *
from datetime import datetime
from django.db.models import Avg, Sum, Max, Min
from .forms import *


def index(request):
    st = 'name'
    all_people = User.objects.all()
    people = User.objects.order_by(st) & User.objects.order_by('age')
    chel = User.objects.aggregate(Avg('age'))
    # people = User.objects.filter(age=32) | User.objects.filter(name='Евгений')
    return render(request, 'app/index.html', context={'people': people, 'chel': chel})


def create(request):
    if request.method == 'POST':
        form = AddMan(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            User.objects.create(name=name, age=age)
            return redirect('home')
        else:
            form = AddMan()
            return render(request, 'app/create.html', context={'form': form})
    else:
        form = AddMan()
        return render(request, 'app/create.html', context={'form': form})


def user(request, id):
    try:
        i = User.objects.get(id=id)
        return render(request, 'app/user.html', context={'i': i})
    except:
        return redirect('home')


def update(request, id):
    try:
        i = User.objects.get(id=id)
        if request.method == 'POST':
            i.name = request.POST.get('name')
            i.age = request.POST.get('age')
            i.save()
            return redirect('home')
        else:
            return render(request, 'app/update.html', context={'i': i})
    except:
        return redirect('create')


def delete(request, id):
    try:
        i = User.objects.get(id=id)
        i.delete()
        return redirect('home')
    except:
        return redirect('home')

def order(request):
    create_orders()
    orders = Order.objects.filter(datetime__month=6, datetime__day=24)
    return render(request, 'app/orders.html', context={'orders': orders})


def create_orders():
    if Order.objects.count() < 5:
        Order.objects.create(datetime=datetime(2020, 6, 24, 12, 23, 55))
        Order.objects.create(datetime=datetime(2021, 4, 16, 12, 23, 55))
        Order.objects.create(datetime=datetime(2022, 10, 3, 12, 23, 55))
        Order.objects.create(datetime=datetime(2023, 11, 13, 12, 23, 55))
