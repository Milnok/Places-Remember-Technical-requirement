from django.contrib import admin
from django.urls import path, include
from places_remember import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/vk/login', include('allauth.urls')),

    path('', views.home, name='home'),
    path('logout/', views.logoutuser, name='logoutuser'),
]
