from django.contrib import admin
from . models import Makale

@admin.register(Makale)
class Makale(admin.ModelAdmin):
    list_display = ('isim','erisim', 'tarih',)
    list_filter = ('erisim',)
    search_fields = ('isim', 'aciklama')