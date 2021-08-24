from django.contrib import admin
from . models import Galeri

@admin.register(Galeri)
class GaleriAdmin(admin.ModelAdmin):
    list_display = ('resim_isim','erisim', )
    list_filter = ('erisim',)
    search_fields = ('resim_isim', 'resim_aciklama')
