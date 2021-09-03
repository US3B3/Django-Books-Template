from django.contrib import admin
from . models import İletisim, Ayarlar

@admin.register(İletisim)
class İletisim(admin.ModelAdmin):
    list_display = ('email', 'ad_soyad','okundu')
    list_filter = ('okundu',)
    search_fields = ('ad_soyad','email')

@admin.register(Ayarlar)
class Ayarlar(admin.ModelAdmin):
    list_display = ('anasayfa_banner_baslik',)
