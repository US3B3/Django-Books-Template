from django.contrib import admin
from . models import Makale, Kategori

@admin.register(Makale)
class Makale(admin.ModelAdmin):
    list_display = ('isim','erisim', 'tarih',)
    list_filter = ('erisim','basMakale', 'taliMakale')
    search_fields = ('isim', 'aciklama')

@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('isim',)}