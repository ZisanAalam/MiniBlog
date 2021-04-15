from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.Home, name='home'), 
    path('about/', views.About, name='about'), 
    path('contact/', views.Contact, name='contact'), 
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('addpost/', views.add_post, name='addpost'),
    path('editpost/<int:id>', views.edit_post, name='editpost'),
    path('deletepost/<int:id>', views.delete_post, name='deletepost'),
    path('profile/', views.user_profile, name='profile'),
]