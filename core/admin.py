from django.contrib import admin

from .models import Contact
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','full_name','email','message','timestamp']
    list_display_links = ['id','full_name','email','message','timestamp']
    readonly_fields = ['timestamp',]
    search_fields = ['full_name','email','message']
    list_filter = ['timestamp',]
    list_per_page = 20
