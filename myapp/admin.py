from django.contrib import admin
from .models import Custom
# Register your models here.

@admin.register(Custom)
class CUstomAdmin(admin.ModelAdmin):
    list_display = ['nomi', 'narxi']
    list_filter = ['yaroq_sana']
    search_fields = ['nomi', 'narxi']
