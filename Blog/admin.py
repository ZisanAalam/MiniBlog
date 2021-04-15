from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Post, Profile

# Register your models here.
@admin.register(Post)
class PostModelAdmin(ModelAdmin):
    list_display = ['id', 'title', 'desc']

@admin.register(Profile)
class ProfileAdmin(ModelAdmin):
    list_display = ['user', 'phone', 'age','image']