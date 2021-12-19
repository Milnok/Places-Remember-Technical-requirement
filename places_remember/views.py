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
    context = get_my_memories_context(request)
    return render(request, 'places_remember/my_memories.html', context)


@login_required
def memory_details(request, memory_pk):
    # Viewing or modifying existing memories
    if request.method == 'GET':
        context = get_memory_detail_context(request, memory_pk)
        return render(request, 'places_remember/create_memory.html', context)
    else:
        edit_place_obj(request, memory_pk)
        return redirect('my_memories')


@login_required
def create_memory(request):
    # Creating new memory
    if request.method == 'GET':
        return render(request, 'places_remember/create_memory.html', {'form': PlaceForm})
    else:
        create_place_obj(request)
        return redirect('my_memories')


@login_required
def delete_memory(request, memory_pk):
    if request.method == 'POST':
        memory = get_object_or_404(Place, pk=memory_pk, user=request.user)
        memory.delete()
        return redirect('my_memories')


def create_place_obj(request):
    form = PlaceForm(request.POST)
    if not form.is_valid():
        raise Http404('Слишком длинный заголовок')
    place = form.save(commit=False)
    place.user = request.user
    coords = request.POST['coords'].split(',')
    place.latitude = coords[0]
    place.longitude = coords[1]
    place.save()
    return place


def edit_place_obj(request, memory_pk):
    form = PlaceForm(request.POST)
    if not form.is_valid():
        raise Http404('Слишком много текста, думаю можно и поменьше')
    place = get_object_or_404(Place, pk=memory_pk, user=request.user)
    place.title = request.POST['title']
    place.discription = request.POST['discription']
    coords = request.POST['coords'].split(',')
    place.latitude = coords[0]
    place.longitude = coords[1]
    place.save()


def get_memory_detail_context(request, memory_pk):
    memory = get_object_or_404(Place, pk=memory_pk, user=request.user)
    form = PlaceForm(instance=memory)
    coords = str(memory.latitude) + ',' + str(memory.longitude)
    context = {
        'memory': memory,
        'form': form,
        'coords': coords,
    }
    return context


def get_my_memories_context(request):
    context = {}
    all_memories = Place.objects.filter(user=request.user)
    if all_memories is not None:
        context['memories'] = all_memories
    return context
