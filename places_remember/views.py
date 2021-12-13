from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'places_remember/home.html')


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    else:
        logout(request)
        return redirect('home')
