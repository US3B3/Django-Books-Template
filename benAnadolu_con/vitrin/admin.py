from django.contrib import admin
from . models import Vitrin

@admin.register(Vitrin)
class VitrinAdmin(admin.ModelAdmin):
    list_display = ('kitap_isim','erisim', )
    list_filter = ('erisim',)
    search_fields = ('kitap_isim', 'kitap_aciklama')
