from django.contrib import admin

from .models import Event, Application

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id','name','location','date','time','price','organizer','timestamp']
    list_display_links = ['id','name']
    list_per_page = 20
    search_fields = ['name',]
    list_filter = ['date','timestamp']

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id','full_name','email','phone_number','address','timestamp']
    list_display_links = ['id','full_name','email']
    search_fields = ['full_name','email']
    list_filter = ['event','timestamp']
    list_per_page = 20