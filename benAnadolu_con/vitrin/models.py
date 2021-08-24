from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField



class Vitrin(models.Model):

    kitap_isim = models.CharField(max_length=100, unique=True, verbose_name="Kitap Başlık", null=True)
    kitap_aciklama = RichTextUploadingField(blank=True, null=True)
    kitap_resim = models.ImageField(upload_to="makale/%Y/%m/%d/", default="varsayilan.jpg")
    erisim = models.BooleanField(default=True)
    tarih = models.DateTimeField(auto_now=True)
    kitap_alt = models.CharField(max_length=100, unique=True, verbose_name="Alternatif metin", null=True)
    yazar = models.CharField(max_length=100, unique=True, verbose_name="Yazar", null=True)

    def __str__(self):
        return self.kitap_isim
