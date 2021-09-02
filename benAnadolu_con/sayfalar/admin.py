from django.contrib import admin
from . models import İletisim

@admin.register(İletisim)
class İletisim(admin.ModelAdmin):
    list_display = ('email', 'ad_soyad','okundu')
    list_filter = ('okundu',)
    search_fields = ('ad_soyad','email')
