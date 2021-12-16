from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .forms import PlaceForm
from .models import Place


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
    all_memories = Place.objects.filter(user=request.user)
    context = {}
    if all_memories != None:
        context['memories'] = all_memories
    return render(request, 'places_remember/my_memories.html', context)


@login_required
def memory_details(request, memory_pk):
    # Viewing or modifying existing memories
    if request.method == 'GET':
        memory = get_object_or_404(Place, pk=memory_pk, user=request.user)
        form = PlaceForm(instance=memory)
        coords = str(memory.latitude) + ',' + str(memory.longitude)
        context = {
            'memory': memory,
            'form': form,
            'coords': coords,
        }
        return render(request, 'places_remember/create_memory.html', context)
    else:
        create_or_edit_place(request, memory_pk)
        return redirect('my_memories')


@login_required
def create_memory(request):
    # Creating new memory
    if request.method == 'GET':
        return render(request, 'places_remember/create_memory.html', {'form': PlaceForm})
    else:
        create_or_edit_place(request)
        return redirect('my_memories')


@login_required
def delete_memory(request, memory_pk):
    if request.method == 'POST':
        memory = get_object_or_404(Place, pk=memory_pk, user=request.user)
        memory.delete()
        return redirect('my_memories')


@login_required
def create_or_edit_place(request, memory_pk=None):
    form = PlaceForm(request.POST)
    if not form.is_valid():
        raise Http404('Слишком много текста, думаю можно и поменьше')
    if memory_pk is None:
        place = form.save(commit=False)
        place.user = request.user
    else:
        place = get_object_or_404(Place, pk=memory_pk, user=request.user)
        place.title = request.POST['title']
        place.discription = request.POST['discription']
    coords = request.POST['coords'].split(',')
    place.latitude = coords[0]
    place.longitude = coords[1]
    place.save()
