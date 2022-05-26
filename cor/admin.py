from django.contrib import admin
from cor.models import Contact1
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'adress', 'messages']
    list_filter = ['sent_at']
    search_fields = ['name', 'email', 'adress', 'messages']
    list_editable = ['email']
admin.site.register(Contact1, ContactAdmin)