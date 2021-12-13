from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def handle_404(request, exception):
    return redirect('home')


def home(request):
    if request.user.is_authenticated:
        return redirect('my_memories')
    else:
        return render(request, 'socialaccount/home.html')


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    else:
        logout(request)
        return redirect('home')


@login_required
def my_memories(request):
    return render(request, 'places_remember/my_memories.html')



@login_required
def create_memory(request):
    return render(request, 'places_remember/create_memory.html')
