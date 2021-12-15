from django.contrib import admin
from django.urls import path, include
from places_remember import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/vk/login', include('allauth.urls')),

    path('', views.home, name='home'),
    path('logout/', views.logoutuser, name='logoutuser'),

    path('my_memories/', views.my_memories, name='my_memories'),
    path('my_memories/<int:memory_pk>', views.memory_details, name='details'),
    path('my_memories/<int:memory_pk>/delete', views.delete_memory, name='delete'),
    path('create_memory/', views.create_memory, name='create_memory'),

]
handler404 = 'places_remember.views.handle_404'
