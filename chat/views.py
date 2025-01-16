
from .models import Message
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('chat:chat_home')
    else:
        form = UserCreationForm()
        
    return render(request, 'signup.html', {'form': form})


def chat_home(request):
    users = user.objects.exclude(id=request.user.id)
    return render(request, 'chat_home.html', {'users': users})
