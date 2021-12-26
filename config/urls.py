from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.urls import path, include
from places_remember.views import LogoutUser, Home, MemoryDetails, MyMemories, DeleteMemory, CreateMemory


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/vk/login', include('allauth.urls')),

    path('', Home.as_view(), name='home'),
    path('logout/', login_required(LogoutUser.as_view()), name='logoutuser'),

    path('my_memories/', login_required(MyMemories.as_view()), name='my_memories'),
    path('my_memories/<int:memory_pk>', login_required(MemoryDetails.as_view()), name='details'),
    path('my_memories/<int:memory_pk>/delete', login_required(DeleteMemory.as_view()), name='delete'),
    path('create_memory/', login_required(CreateMemory.as_view()), name='create_memory'),

]
handler404 = 'places_remember.views.handle_404'
