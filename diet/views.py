from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm, ChatForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.template import RequestContext

def index(request):
    return render(request, 'diet/index.html')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('index')
    else:
        form = UserForm()
        return render(request, 'diet/signup.html', {'form': form})


def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'diet/signin.html', {'form': form})


# def Chat(request):
#     if request.method == "POST":
#         form = ChatForm(request.POST)
#     if form.is_valid():
#         chat_text = form.save(commit = False)
#         chat_text.name_id = User.objects.get(username = request.user.get_username())
#         chat_text.generate()
#     return redirect('index')


# def chat_room(request, label):
#     # If the room with the given label doesn't exist, automatically create it
#     # upon first visit (a la etherpad).
#     room, created = Room.objects.get_or_create(label=label)

#     # We want to show the last 50 messages, ordered most-recent-last
#     messages = reversed(room.messages.order_by('-timestamp')[:50])

#     return render(request, "chat/room.html", {
#         'room': room,
#         'messages': messages,
#     })