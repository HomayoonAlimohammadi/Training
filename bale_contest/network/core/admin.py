from django.contrib import admin
from .models import CustomeUser, Post 

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']

admin.site.register(CustomeUser, UserAdmin)
admin.site.register(Post)