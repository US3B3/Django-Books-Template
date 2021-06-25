from django.contrib import admin
from . models import VideoDers

@admin.register(VideoDers)
class VideoDersAdmin(admin.ModelAdmin):
    list_display = ('isim','erisim', 'tarih',)
    list_filter = ('erisim',)
    search_fields = ('isim', 'aciklama')
