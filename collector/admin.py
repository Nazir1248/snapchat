# collector/admin.py
from django.contrib import admin
from .models import Credential

@admin.register(Credential)
class CredentialAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('username',)