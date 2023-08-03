from django.contrib import admin

from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','full_name','email','date_joined']
    list_display_links = ['id','full_name','email','date_joined']
    search_fields = ['full_name','email']
    list_per_page = 20