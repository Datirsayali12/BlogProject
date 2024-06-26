from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf import settings
urlpatterns = [
    path('',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('addPost',views.addPost,name='addPost'),
    path('search',views.search,name='search'),
    path('signup',views.signup,name='signup'),
    path('Login',views.handleLogin,name='Login'),
    path('Logout',views.Logout,name='Logout'),
    path('profile/<str:user_name>/',views.profile,name='profile'),




]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)