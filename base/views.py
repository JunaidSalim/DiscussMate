from django.shortcuts import render,redirect
from django.db.models import Q
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import RoomForm,userForm,CustomUserCreationForm
from django.db.models import Count

# Create your views here.
def home(request):
    q = request.GET.get('q') if request.GET.get('q')!=None else ''
    topics = Topic.objects.annotate(room_count=Count('room')).order_by('-room_count')
    rooms = Room.objects.filter(Q(topic__name__icontains=q) | Q(description__icontains=q) | Q(name__icontains=q))
    room_count = rooms.count()
    room_messages = Message.objects.all().filter(Q(room__topic__name__icontains = q))
    context = {
        "rooms":rooms,
        "topics":topics,
        "room_count":room_count,
        "room_messages":room_messages,
        }
    return render(request,'base/home.html',context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all()
    participants = room.participants.all()
    if request.method=='POST':
        message = Message.objects.create(
            user = request.user, room = room, body = request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room',pk=room.id)
    context = {"room":room,
               "room_messages":room_messages,
               "participants":participants,
               }
    return render(request,'base/room.html',context)

@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    topics = Topic.objects.all()
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic,created = Topic.objects.get_or_create(name=topic_name)
        Room.objects.create(
            host = request.user,
            topic=topic,
            name = request.POST.get('name'),
            description = request.POST.get('description')
        )
        return redirect('home')

    context = {
        'form':form,
        'topics':topics,
    }
    return render(request,'base/room_form.html',context)

@login_required(login_url='login')
def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    topics = Topic.objects.all()
    form = RoomForm(instance=room)
    if request.user!=room.host:
        messages.error(request,'Access Denied')
        return redirect('home')
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic,created = Topic.objects.get_or_create(name=topic_name)
        room.name  = request.POST.get('name')        
        room.topic = topic
        room.description = request.POST.get('description')        
        room.save()         
        return redirect('home')
    context = {
        'topics':topics,
        'form':form,
        'room':room,
    }
    return render(request,'base/room_form.html',context)

@login_required(login_url='login')
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.user!=room.host:
        messages.error(request,'Access Denied')
        return redirect('home')

    if request.method=='POST':
        room.delete()
        return redirect('home')
    context = {'obj':room}
    return render(request,'base/delete.html',context)

@login_required(login_url='login')
def deleteMessage(request,pk):
    message = Message.objects.get(id=pk)
    if request.user!=message.user:
        messages.error(request,'Access Denied')
        return redirect('room')

    if request.method=='POST':
        message.delete()
        return redirect('home')
    context = {'obj':message}
    return render(request,'base/delete.html',context)
    
def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=="POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,"User Does Not Exists")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Invalid Credentials")
    context = {"page":page}
    return render(request,'base/login_register.html',context)

def registerPage(request):
    form = CustomUserCreationForm()
    if request.method=="POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            messages.info(request,'User has been registered!')
            return redirect('home')
        else:
            for error in list(form.errors.values()):
                messages.error(request,error)
            return redirect('register')
    context = {
        "form":form}
    return render(request,'base/login_register.html',context)


@login_required(login_url='login')
def logoutPage(request):
    logout(request)
    messages.info(request,"Successfully Logged Out")
    return redirect('home')

def userProfile(request,pk):
    user = User.objects.get(id=pk)    
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()
    context = {
        'user':user,
        'rooms':rooms,
        'room_messages':room_messages,
        'topics':topics,
    }
    return render(request,'base/profile.html',context)

@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = userForm(instance=user)
    if request.method == "POST":
        form = userForm(request.POST,request.FILES,instance = user)
        if form.is_valid():
            form.save()
            return redirect('profile',pk=user.id)
    context = {
        'form':form
    }
    return render(request,'base/update-user.html',context)

def topicsPage(request):
    q = request.GET.get('q') if request.GET.get('q')!=None else ''
    topics = Topic.objects.filter(name__icontains=q)
    context = {
        'topics':topics,
    }
    return render(request,'base/topics.html',context)

def activityPage(request):
    room_messages = Message.objects.all().order_by('-created','-updated')
    context = {
        'room_messages': room_messages
    }
    return render(request,'base/activity.html',context)
