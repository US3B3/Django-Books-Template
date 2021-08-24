from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField



class Galeri(models.Model):

    resim_isim = models.CharField(max_length=100, unique=True, verbose_name="Resim Başlık", null=True)
    resim_aciklama = RichTextUploadingField(blank=True, null=True)
    resim = models.ImageField(upload_to="makale/%Y/%m/%d/", default="varsayilan.jpg")
    erisim = models.BooleanField(default=True)
    tarih = models.DateTimeField(auto_now=True)
    resim_alt = models.CharField(max_length=100, unique=True, verbose_name="Alternatif metin", null=True)

    def __str__(self):
        return self.resim_isim
