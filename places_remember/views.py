from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import PlaceForm


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
    if request.method == 'GET':
        return render(request, 'places_remember/create_memory.html', {'form': PlaceForm})
    else:
        form = PlaceForm(request.POST)
        newplace = form.save(commit=False)
        newplace.user = request.user
        coords = request.POST['coords'].split(',')
        newplace.latitude = coords[0]
        newplace.longitude = coords[1]
        newplace.save()
        return redirect('my_memories')
