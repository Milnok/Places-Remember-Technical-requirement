from django.shortcuts import redirect, reverse
from django.contrib.auth import logout
from django.http import Http404
from django.views.generic import ListView, CreateView, View, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PlaceForm
from .models import Place


class Home(TemplateView):
    template_name = 'socialaccount/home.html'


class LogoutUser(View):
    def get(self, request):
        logout(request)
        return redirect('home')


class MyMemories(ListView):
    model = Place
    template_name = 'places_remember/my_memories.html'
    context_object_name = 'memories'

    def get_queryset(self):
        return Place.objects.filter(user=self.request.user)


class MemoryDetails(UpdateView):
    model = Place
    form_class = PlaceForm
    template_name = 'places_remember/create_memory.html'
    pk_url_kwarg = 'memory_pk'
    success_url = '/my_memories'
    context_object_name = 'memory'

    def get_object(self, queryset=None):
        obj = super(MemoryDetails, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj


class CreateMemory(CreateView):
    form_class = PlaceForm
    template_name = 'places_remember/create_memory.html'
    success_url = reverse_lazy('my_memories')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect('my_memories')


class DeleteMemory(DeleteView):
    model = Place
    pk_url_kwarg = 'memory_pk'

    def get_object(self, queryset=None):
        obj = super(DeleteMemory, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

    def get_success_url(self):
        return reverse('my_memories')
